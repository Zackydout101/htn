import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

def add_to_redis(key, value):
    """
    Add data to Redis.
    
    Parameters:
    - key: The key under which the value is stored in Redis.
    - value: The value to store in Redis.
    """
    try:
        # Set the key-value pair in Redis
        r.set(key, value)
        print(f"Data set: {key} -> {value}")

        # Retrieve the value to confirm it was set
        retrieved_value = r.get(key)
        print(f"Data retrieved: {key} -> {retrieved_value.decode('utf-8')}")
    except redis.ConnectionError:
        print("Failed to connect to Redis.")

# Example usage
key = 'hola'
value = 'jjnjnjnjnjnj'
add_to_redis(key, value)
