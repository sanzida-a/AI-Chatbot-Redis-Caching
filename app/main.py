import os
import time
import logging
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import cache
import ai_engine

load_dotenv()

app = FastAPI(title="AI Chatbot with Redis Caching")
logger = logging.getLogger("chatbot")
logging.basicConfig(level=logging.INFO)

class ChatRequest(BaseModel):
    query: str

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = round(time.time() - start_time, 3)
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.on_event("startup")
def on_startup():
    cache.get_redis_client()
    logger.info("🚀 App started with Redis and Gemini ready.")

@app.post("/chat")
async def chat(request: ChatRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    
    key = f"chat:{query.lower()}"
    cached_response = await cache.get_cached_response(key)
    
    if cached_response:
        logger.info(f"Cache HIT for: {query}")
        return {"query": query, "response": cached_response, "cached": True}
    
    logger.info(f"Cache MISS for: {query}")
    ai_response = await ai_engine.generate_ai_response(query)
    await cache.set_cached_response(key, ai_response)
    
    return {"query": query, "response": ai_response, "cached": False}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
