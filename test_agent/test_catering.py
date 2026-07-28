import asyncio

from agents.catering_agent import catering_agent


async def main():

    response = await catering_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": """
Find the best catering company
for 100 wedding guests in Paris.
"""
                }
            ]
        }
    )

    print(response["structured_response"])


if __name__ == "__main__":
    asyncio.run(main())