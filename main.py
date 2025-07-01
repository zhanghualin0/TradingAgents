from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from dotenv import load_dotenv
import os
load_dotenv()

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = os.getenv("LLM_PROVIDER", "openai")  # Use a different model
config["backend_url"] = os.getenv("BACKEND_URL", "https://api.openai.com/v1")  # Use a different backend
config["deep_think_llm"] = os.getenv("DEEP_THINK_LLM", "o4-mini")  # Use a different model
config["quick_think_llm"] = os.getenv("QUICK_THINK_LLM", "gpt-4o-mini")  # Use a different model
config["max_debate_rounds"] = int(os.getenv("MAX_DEBATE_ROUNDS", 1))  # Increase debate rounds
config["online_tools"] = bool(os.getenv("ONLINE_TOOLS", "True"))  # Increase debate rounds

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
