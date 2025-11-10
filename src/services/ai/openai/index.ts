// AI Service Interfaces
import { OpenAI } from 'openai';
import Anthropic from '@anthropic-ai/sdk';
import { GoogleGenerativeAI } from '@google/generative-ai';
// Optional package - uncomment and install if needed
// import { OpenAIClient } from '@azure/openai';
const OpenAIClient = class {
  constructor(endpoint: string, apiKey: string) {}
} as any;

export interface AIProvider {
  chatCompletion(messages: ChatMessage[], options?: ChatOptions): Promise<ChatResponse>;
  generateText(prompt: string, options?: TextOptions): Promise<TextResponse>;
  generateImage(prompt: string, options?: ImageOptions): Promise<ImageResponse>;
  generateEmbeddings(input: string, options?: EmbeddingOptions): Promise<EmbeddingResponse>;
}

export interface ChatMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export interface ChatOptions {
  model?: string;
  temperature?: number;
  maxTokens?: number;
  topP?: number;
  frequencyPenalty?: number;
  presencePenalty?: number;
  stop?: string[];
}

export interface ChatResponse {
  content: string;
  model: string;
  usage: TokenUsage;
  finishReason: string;
}

export interface TextOptions {
  model?: string;
  temperature?: number;
  maxTokens?: number;
  topP?: number;
}

export interface TextResponse {
  text: string;
  model: string;
  usage: TokenUsage;
}

export interface ImageOptions {
  model?: string;
  size?: string;
  quality?: string;
  style?: string;
  n?: number;
}

export interface ImageResponse {
  images: ImageData[];
  model: string;
}

export interface ImageData {
  url: string;
  base64?: string;
  revisedPrompt?: string;
}

export interface EmbeddingOptions {
  model?: string;
}

export interface EmbeddingResponse {
  embeddings: number[];
  model: string;
  usage: TokenUsage;
}

export interface TokenUsage {
  promptTokens: number;
  completionTokens: number;
  totalTokens: number;
}

// OpenAI Service Implementation
export class OpenAIService implements AIProvider {
  private client: OpenAI;

  constructor(config: OpenAIConfig) {
    this.client = new OpenAI({
      apiKey: config.apiKey,
      organization: config.organization
    });
  }

  async chatCompletion(messages: ChatMessage[], options?: ChatOptions): Promise<ChatResponse> {
    try {
      const response = await this.client.chat.completions.create({
        model: options?.model || 'gpt-4',
        messages: messages.map(msg => ({
          role: msg.role,
          content: msg.content
        })),
        temperature: options?.temperature || 0.7,
        max_tokens: options?.maxTokens || 1000,
        top_p: options?.topP,
        frequency_penalty: options?.frequencyPenalty,
        presence_penalty: options?.presencePenalty,
        stop: options?.stop
      });

      const choice = response.choices[0];
      
      return {
        content: choice.message.content || '',
        model: response.model,
        usage: {
          promptTokens: response.usage?.prompt_tokens || 0,
          completionTokens: response.usage?.completion_tokens || 0,
          totalTokens: response.usage?.total_tokens || 0
        },
        finishReason: choice.finish_reason || 'stop'
      };
    } catch (error) {
      throw new AIError('OpenAI chat completion failed', error as Error);
    }
  }

  async generateText(prompt: string, options?: TextOptions): Promise<TextResponse> {
    try {
      const response = await this.client.completions.create({
        model: options?.model || 'text-davinci-003',
        prompt,
        temperature: options?.temperature || 0.7,
        max_tokens: options?.maxTokens || 1000,
        top_p: options?.topP
      });

      return {
        text: response.choices[0].text || '',
        model: response.model,
        usage: {
          promptTokens: response.usage?.prompt_tokens || 0,
          completionTokens: response.usage?.completion_tokens || 0,
          totalTokens: response.usage?.total_tokens || 0
        }
      };
    } catch (error) {
      throw new AIError('OpenAI text generation failed', error as Error);
    }
  }

  async generateImage(prompt: string, options?: ImageOptions): Promise<ImageResponse> {
    try {
      const response = await this.client.images.generate({
        model: options?.model || 'dall-e-3',
        prompt,
        size: options?.size as any || '1024x1024',
        quality: options?.quality as any || 'standard',
        n: options?.n || 1,
        style: options?.style as any
      });

      return {
        images: (response.data || []).map((img: any) => ({
          url: img.url || '',
          revisedPrompt: img.revised_prompt
        })),
        model: (response as any).model || 'dall-e-3'
      };
    } catch (error) {
      throw new AIError('OpenAI image generation failed', error as Error);
    }
  }

  async generateEmbeddings(input: string, options?: EmbeddingOptions): Promise<EmbeddingResponse> {
    try {
      const response = await this.client.embeddings.create({
        model: options?.model || 'text-embedding-ada-002',
        input
      });

      return {
        embeddings: response.data[0].embedding,
        model: response.model,
        usage: {
          promptTokens: response.usage?.prompt_tokens || 0,
          completionTokens: 0,
          totalTokens: response.usage?.total_tokens || 0
        }
      };
    } catch (error) {
      throw new AIError('OpenAI embedding generation failed', error as Error);
    }
  }
}

// Anthropic Service Implementation
export class AnthropicService implements AIProvider {
  private client: Anthropic;

  constructor(config: AnthropicConfig) {
    this.client = new Anthropic({
      apiKey: config.apiKey
    });
  }

  async chatCompletion(messages: ChatMessage[], options?: ChatOptions): Promise<ChatResponse> {
    try {
      const response = await (this.client as any).messages.create({
        model: options?.model || 'claude-3-sonnet-20240229',
        max_tokens: options?.maxTokens || 1000,
        temperature: options?.temperature || 0.7,
        messages: messages.map(msg => ({
          role: msg.role as 'user' | 'assistant',
          content: msg.content
        }))
      });

      return {
        content: response.content[0].text || '',
        model: response.model,
        usage: {
          promptTokens: response.usage.input_tokens,
          completionTokens: response.usage.output_tokens,
          totalTokens: response.usage.input_tokens + response.usage.output_tokens
        },
        finishReason: response.stop_reason || 'stop'
      };
    } catch (error) {
      throw new AIError('Anthropic chat completion failed', error as Error);
    }
  }

  async generateText(prompt: string, options?: TextOptions): Promise<TextResponse> {
    try {
      const response = await this.client.completions.create({
        model: options?.model || 'claude-3-sonnet-20240229',
        max_tokens_to_sample: options?.maxTokens || 1000,
        temperature: options?.temperature || 0.7,
        prompt
      });

      return {
        text: response.completion || '',
        model: response.model,
        usage: {
          promptTokens: (response as any).usage?.input_tokens || 0,
          completionTokens: (response as any).usage?.output_tokens || 0,
          totalTokens: ((response as any).usage?.input_tokens || 0) + ((response as any).usage?.output_tokens || 0)
        }
      };
    } catch (error) {
      throw new AIError('Anthropic text generation failed', error as Error);
    }
  }

  async generateImage(prompt: string, options?: ImageOptions): Promise<ImageResponse> {
    throw new AIError('Anthropic does not support image generation');
  }

  async generateEmbeddings(input: string, options?: EmbeddingOptions): Promise<EmbeddingResponse> {
    throw new AIError('Anthropic does not support embeddings');
  }
}

// Google AI Service Implementation
export class GoogleAIService implements AIProvider {
  private genAI: GoogleGenerativeAI;

  constructor(config: GoogleAIConfig) {
    this.genAI = new GoogleGenerativeAI(config.apiKey);
  }

  async chatCompletion(messages: ChatMessage[], options?: ChatOptions): Promise<ChatResponse> {
    try {
      const model = this.genAI.getGenerativeModel({ 
        model: options?.model || 'gemini-pro' 
      });

      const chat = model.startChat({
        history: messages.slice(0, -1).map(msg => ({
          role: msg.role === 'assistant' ? 'model' : 'user',
          parts: [{ text: msg.content }]
        }))
      });

      const result = await chat.sendMessage(messages[messages.length - 1].content);
      const response = await result.response;

      return {
        content: response.text() || '',
        model: options?.model || 'gemini-pro',
        usage: {
          promptTokens: 0, // Google AI doesn't provide detailed usage
          completionTokens: 0,
          totalTokens: 0
        },
        finishReason: 'stop'
      };
    } catch (error) {
      throw new AIError('Google AI chat completion failed', error as Error);
    }
  }

  async generateText(prompt: string, options?: TextOptions): Promise<TextResponse> {
    try {
      const model = this.genAI.getGenerativeModel({ 
        model: options?.model || 'gemini-pro' 
      });

      const result = await model.generateContent(prompt);
      const response = await result.response;

      return {
        text: response.text() || '',
        model: options?.model || 'gemini-pro',
        usage: {
          promptTokens: 0,
          completionTokens: 0,
          totalTokens: 0
        }
      };
    } catch (error) {
      throw new AIError('Google AI text generation failed', error as Error);
    }
  }

  async generateImage(prompt: string, options?: ImageOptions): Promise<ImageResponse> {
    try {
      const model = this.genAI.getGenerativeModel({ 
        model: options?.model || 'imagen-2' 
      });

      const result = await model.generateContent(prompt);
      const response = await result.response;

      // Google AI image generation returns different format
      return {
        images: [{
          url: response.text() || '',
          base64: response.text() || ''
        }],
        model: options?.model || 'imagen-2'
      };
    } catch (error) {
      throw new AIError('Google AI image generation failed', error as Error);
    }
  }

  async generateEmbeddings(input: string, options?: EmbeddingOptions): Promise<EmbeddingResponse> {
    try {
      const model = this.genAI.getGenerativeModel({ 
        model: options?.model || 'text-embedding-004' 
      });

      const result = await model.embedContent(input);
      const embedding = result.embedding;

      return {
        embeddings: embedding.values || [],
        model: options?.model || 'text-embedding-004',
        usage: {
          promptTokens: 0,
          completionTokens: 0,
          totalTokens: 0
        }
      };
    } catch (error) {
      throw new AIError('Google AI embedding generation failed', error as Error);
    }
  }
}

// Azure AI Service Implementation
export class AzureAIService implements AIProvider {
  private client: any;

  constructor(config: AzureAIConfig) {
    this.client = new OpenAIClient(config.endpoint, config.apiKey);
  }

  async chatCompletion(messages: ChatMessage[], options?: ChatOptions): Promise<ChatResponse> {
    try {
      const response = await this.client.getChatCompletions(
        options?.model || 'gpt-4',
        messages.map(msg => ({
          role: msg.role as 'system' | 'user' | 'assistant',
          content: msg.content
        })),
        {
          temperature: options?.temperature || 0.7,
          maxTokens: options?.maxTokens || 1000,
          topP: options?.topP,
          frequencyPenalty: options?.frequencyPenalty,
          presencePenalty: options?.presencePenalty,
          stop: options?.stop
        }
      );

      const choice = response.choices[0];
      
      return {
        content: choice.message?.content || '',
        model: response.model || options?.model || 'gpt-4',
        usage: {
          promptTokens: response.usage?.promptTokens || 0,
          completionTokens: response.usage?.completionTokens || 0,
          totalTokens: response.usage?.totalTokens || 0
        },
        finishReason: choice.finishReason || 'stop'
      };
    } catch (error) {
      throw new AIError('Azure AI chat completion failed', error as Error);
    }
  }

  async generateText(prompt: string, options?: TextOptions): Promise<TextResponse> {
    try {
      const response = await this.client.getCompletions(
        options?.model || 'text-davinci-003',
        [prompt],
        {
          temperature: options?.temperature || 0.7,
          maxTokens: options?.maxTokens || 1000,
          topP: options?.topP
        }
      );

      return {
        text: response.choices[0].text || '',
        model: response.model || options?.model || 'text-davinci-003',
        usage: {
          promptTokens: response.usage?.promptTokens || 0,
          completionTokens: response.usage?.completionTokens || 0,
          totalTokens: response.usage?.totalTokens || 0
        }
      };
    } catch (error) {
      throw new AIError('Azure AI text generation failed', error as Error);
    }
  }

  async generateImage(prompt: string, options?: ImageOptions): Promise<ImageResponse> {
    try {
      const response = await this.client.getImages(
        options?.model || 'dall-e-3',
        prompt,
        {
          size: options?.size as any || '1024x1024',
          quality: options?.quality as any || 'standard',
          n: options?.n || 1,
          style: options?.style as any
        }
      );

      return {
        images: response.data.map((img: any) => ({
          url: img.url || '',
          revisedPrompt: img.revisedPrompt
        })),
        model: (response as any).model || options?.model || 'dall-e-3'
      };
    } catch (error) {
      throw new AIError('Azure AI image generation failed', error as Error);
    }
  }

  async generateEmbeddings(input: string, options?: EmbeddingOptions): Promise<EmbeddingResponse> {
    try {
      const response = await this.client.getEmbeddings(
        options?.model || 'text-embedding-ada-002',
        [input]
      );

      return {
        embeddings: response.data[0].embedding,
        model: response.model || options?.model || 'text-embedding-ada-002',
        usage: {
          promptTokens: response.usage?.promptTokens || 0,
          completionTokens: 0,
          totalTokens: response.usage?.totalTokens || 0
        }
      };
    } catch (error) {
      throw new AIError('Azure AI embedding generation failed', error as Error);
    }
  }
}

// AI Service Factory
export class AIServiceFactory {
  static createService(type: string, config: any): AIProvider {
    switch (type) {
      case 'openai':
        return new OpenAIService(config);
      case 'anthropic':
        return new AnthropicService(config);
      case 'google':
        return new GoogleAIService(config);
      case 'azure':
        return new AzureAIService(config);
      default:
        throw new Error(`Unknown AI provider: ${type}`);
    }
  }
}

// Custom Error Classes
export class AIError extends Error {
  cause?: Error;
  constructor(message: string, cause?: Error) {
    super(message);
    this.name = 'AIError';
    this.cause = cause;
  }
}

// Configuration Interfaces
export interface OpenAIConfig {
  apiKey: string;
  organization?: string;
}

export interface AnthropicConfig {
  apiKey: string;
}

export interface GoogleAIConfig {
  apiKey: string;
}

export interface AzureAIConfig {
  endpoint: string;
  apiKey: string;
}
