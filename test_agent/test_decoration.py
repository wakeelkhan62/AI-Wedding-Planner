import asyncio

from agents.decoration_agent import decoration_agent


async def main():

    response = await decoration_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": """
Suggest elegant wedding decorations
for a wedding in Paris.
"""
                }
            ]
        }
    )

    print(response["structured_response"])


if __name__ == "__main__":
    asyncio.run(main())