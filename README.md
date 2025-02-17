# Heeirun's Langgraph QuickStart

## Developer Log

### 2025-02-15

* Initial setup was straight forward. I decided to use uv instead of pip having initially been introduced to it in the quickstart guide for creating a [MCP server](https://modelcontextprotocol.io/quickstart/server). That [speed boost](https://docs.astral.sh/uv/) from Rust is wicked fast!

* I've decided to use a .env file by default to get my Anthropic API key. If the env var does not exist we then request for user input form the CLI

* I moved the State class into its own file. A generic Graph class could be useful to standardize generic graph behavior throughout the agent.

* I had to buy Anthropic API credits to test this. The quickstart defaulted to Sonnet and I switched it to Haiku for cost. I wonder how this affects the useability of these agents.

* I'd love to develop against local llms using Ollama instead of paying for Anthropic credits. Maybe there is value in agent acceptence testing





