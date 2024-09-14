import { createClient } from 'redis';

// Create and configure the Redis client
const redisClient = createClient({
    url: 'redis://localhost:6379' // Update the URL if your Redis server is hosted differently
});

// Connect to the Redis server
redisClient.on('error', (err) => {
    console.error('Redis Client Error:', err);
});

await redisClient.connect();

export async function GET(request) {
    const { searchParams } = new URL(request.url);
    const key = searchParams.get('key'); // Extract the 'hola' parameter from the query string

    console.log(`Received key: ${key}`); // Debug log

    if (!key) {
        return new Response('Key query parameter is required', { status: 400 });
    }

    try {
        // Fetch data from Redis
        const value = await redisClient.get(key);

        console.log(`Value retrieved from Redis: ${value}`); // Debug log

        if (value) {
            return new Response(JSON.stringify({ key, value }), {
                status: 200,
                headers: { 'Content-Type': 'application/json' },
            });
        } else {
            return new Response(JSON.stringify({ message: 'Key not found' }), {
                status: 404,
                headers: { 'Content-Type': 'application/json' },
            });
        }
    } catch (err) {
        console.error('Error fetching data from Redis:', err.message);
        return new Response('Error fetching data', { status: 500 });
    }
}


export async function POST(request) {
    try {
        const data = await request.json(); // Extract JSON data from the request body
        const { key, value } = data;

        if (!key || !value) {
            return new Response('Key and value are required', { status: 400 });
        }

        // Set the key-value pair in Redis
        await redisClient.set(key, value);

        return new Response(JSON.stringify({ message: 'Data uploaded successfully' }), {
            status: 200,
            headers: { 'Content-Type': 'application/json' },
        });
    } catch (err) {
        console.error('Error uploading data to Redis:', err.message);
        return new Response('Error uploading data', { status: 500 });
    }
}