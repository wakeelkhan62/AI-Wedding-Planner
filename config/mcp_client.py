from langchain_mcp_adapters.client import MultiServerMCPClient

print("Loading MCP Client...")

client = MultiServerMCPClient(
    {
        "travel": {
            "command": "npx",
            "args": [
                "-y",
                "@openbnb/mcp-server"
            ],
            "transport": "stdio",
        }
    }
)

print("MCP Client Loaded Successfully")