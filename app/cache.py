import redis.asyncio as redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")  # service name
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

import asyncio

async def wait_for_redis(client, retries=5, delay=1):
    for _ in range(retries):
        try:
            if await client.ping():
                return True
        except Exception:
            await asyncio.sleep(delay)
    raise ConnectionError("Could not connect to Redis")

_redis_client = None

def get_redis_client():
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    return _redis_client

async def get_cached_response(key: str):
    return await get_redis_client().get(key)

async def set_cached_response(key: str, value: str, expire: int = 600):
    await get_redis_client().set(key, value, ex=expire)
