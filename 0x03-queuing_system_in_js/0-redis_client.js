import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Set up event listeners for the Redis client
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});
