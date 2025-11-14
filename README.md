# Autonomous Agent with Automatic Failover

Autonomous AI Agent with automatic failover between multiple free APIs (Groq, TogetherAI, OpenRouter) with integrated backup system using Ollama.

## Features

- **Multi-API Failover**: Automatically switches between Groq, TogetherAI, and OpenRouter APIs
- **Health Check System**: Continuous monitoring of API availability
- **Circuit Breaker Pattern**: Intelligent handling of API failures (3 strikes = 5 min cooldown)
- **Load Balancing**: Weighted random selection based on API priority and performance
- **Local Backup**: Ollama integration for 100% offline fallback
- **Automatic Recovery**: Self-healing system that recovers from service failures
- **Essential Tools**: Web search (Tavily), Code execution (E2B), File I/O (Google Drive), Database ops (Supabase)

## Architecture

### 1. System Principal de Agente
- **Framework**: LangGraph for building the main agent
- **Router Agent**: Selects the best available API
- **Memory**: SQLite or Supabase for history and state

### 2. Free APIs with Priority

```python
API_PROVIDERS = [
    {
        "name": "Groq",
        "models": ["llama3-8b-8192", "mixtral-8x7b-32768"],
        "endpoint": "https://api.groq.com/openai/v1/chat/completions",
        "key_env": "GROQ_API_KEY",
        "priority": 1,
        "fallback_strategy": "auto_retry"
    },
    {
        "name": "TogetherAI",
        "models": ["meta-llama/Llama-3-70b-chat-hf"],
        "endpoint": "https://api.together.xyz/v1/chat/completions",
        "key_env": "TOGETHER_API_KEY",
        "priority": 2,
        "fallback_strategy": "load_balance"
    },
    {
        "name": "OpenRouter",
        "models": ["google/gemini-flash-1.5"],
        "endpoint": "https://openrouter.ai/api/v1/chat/completions",
        "key_env": "OPENROUTER_API_KEY",
        "priority": 3,
        "fallback_strategy": "circuit_breaker"
    }
]
```

## Getting Started

```bash
git clone https://github.com/yourusername/autonomous-agent-failover
cd autonomous-agent-failover
pip install -r requirements.txt
```

## Configuration

Create `.env` file with your API keys:
- GROQ_API_KEY
- TOGETHER_API_KEY
- OPENROUTER_API_KEY

## Version

**Status**: Production Ready
**Last Updated**: 2025-11-14
**Version**: 1.0.0
