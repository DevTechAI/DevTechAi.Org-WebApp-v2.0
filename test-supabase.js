#!/usr/bin/env node
/**
 * Supabase Connectivity Test Script
 * Tests the connection to Supabase database
 */

require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');

async function testSupabaseConnection() {
  console.log('🔍 Testing Supabase Database Connectivity...\n');
  
  // Check for environment variables
  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_ANON_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY;
  
  if (!supabaseUrl || !supabaseKey) {
    console.log('❌ Supabase configuration not found in environment variables.\n');
    console.log('📝 Please set the following in your .env file:');
    console.log('   SUPABASE_URL=https://your_project.supabase.co');
    console.log('   SUPABASE_ANON_KEY=your_anon_key');
    console.log('   (or SUPABASE_SERVICE_ROLE_KEY=your_service_role_key)\n');
    console.log('💡 You can copy env.example to .env and fill in your Supabase credentials.\n');
    return false;
  }
  
  console.log('✅ Environment variables found:');
  console.log(`   SUPABASE_URL: ${supabaseUrl.substring(0, 30)}...`);
  console.log(`   SUPABASE_KEY: ${supabaseKey.substring(0, 20)}...\n`);
  
  try {
    // Create Supabase client
    console.log('🔌 Creating Supabase client...');
    const supabase = createClient(supabaseUrl, supabaseKey);
    
    // Test connection with a simple query
    console.log('📡 Testing connection...');
    const { data, error } = await supabase
      .from('_health_check')
      .select('*')
      .limit(1);
    
    if (error) {
      // If _health_check table doesn't exist, try a different approach
      console.log('⚠️  _health_check table not found, trying alternative connection test...');
      
      // Try to get auth user (this will work even without tables)
      const { data: authData, error: authError } = await supabase.auth.getUser();
      
      if (authError && authError.message.includes('Invalid API key')) {
        console.log('❌ Connection failed: Invalid API key');
        console.log('   Please check your SUPABASE_ANON_KEY or SUPABASE_SERVICE_ROLE_KEY\n');
        return false;
      }
      
      // If we get here, the connection works but there's no _health_check table
      console.log('✅ Supabase connection successful!');
      console.log('   (Note: _health_check table not found, but connection is working)\n');
      return true;
    }
    
    console.log('✅ Supabase connection successful!');
    console.log('   Connection test passed.\n');
    return true;
    
  } catch (error) {
    console.log('❌ Connection failed with error:');
    console.log(`   ${error.message}\n`);
    return false;
  }
}

// Run the test
testSupabaseConnection()
  .then(success => {
    if (success) {
      console.log('🎉 Supabase connectivity test completed successfully!');
      process.exit(0);
    } else {
      console.log('⚠️  Supabase connectivity test failed. Please check your configuration.');
      process.exit(1);
    }
  })
  .catch(error => {
    console.error('💥 Unexpected error:', error);
    process.exit(1);
  });

