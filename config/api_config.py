"""API Configuration for Autonomous Agent"""
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class APIProvider:
    def __init__(self, name: str, models: List[str], endpoint: str, 
                 key_env: str, priority: int, fallback_strategy: str):
        self.name = name
        self.models = models
        self.endpoint = endpoint
        self.api_key = os.getenv(key_env)
        self.priority = priority
        self.fallback_strategy = fallback_strategy
        self.failure_count = 0
        self.last_error_time = None
        self.is_active = True

# API Providers Configuration
API_PROVIDERS = [
    APIProvider(
        name="Groq",
        models=["llama3-8b-8192", "mixtral-8x7b-32768"],
        endpoint="https://api.groq.com/openai/v1/chat/completions",
        key_env="GROQ_API_KEY",
        priority=1,
        fallback_strategy="auto_retry"
    ),
    APIProvider(
        name="TogetherAI",
        models=["meta-llama/Llama-3-70b-chat-hf"],
        endpoint="https://api.together.xyz/v1/chat/completions",
        key_env="TOGETHER_API_KEY",
        priority=2,
        fallback_strategy="load_balance"
    ),
    APIProvider(
        name="OpenRouter",
        models=["google/gemini-flash-1.5"],
        endpoint="https://openrouter.ai/api/v1/chat/completions",
        key_env="OPENROUTER_API_KEY",
        priority=3,
        fallback_strategy="circuit_breaker"
    )
]

# Circuit Breaker Settings
CIRCUIT_BREAKER_THRESHOLD = int(os.getenv("CIRCUIT_BREAKER_THRESHOLD", 3))
CIRCUIT_BREAKER_TIMEOUT = int(os.getenv("CIRCUIT_BREAKER_TIMEOUT", 300))

# Health Check Settings
HEALTH_CHECK_INTERVAL = int(os.getenv("HEALTH_CHECK_INTERVAL", 60))
HEALTH_CHECK_TIMEOUT = 5

# Agent Settings
AGENT_TIMEOUT = int(os.getenv("AGENT_TIMEOUT", 300))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Database Settings
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./agent_memory.db")

# Ollama Settings
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

def get_active_providers() -> List[APIProvider]:
    """Get list of active API providers sorted by priority"""
    active = [p for p in API_PROVIDERS if p.is_active]
    return sorted(active, key=lambda x: x.priority)

def get_best_provider() -> APIProvider:
    """Get the best available provider"""
    active = get_active_providers()
    return active[0] if active else None
