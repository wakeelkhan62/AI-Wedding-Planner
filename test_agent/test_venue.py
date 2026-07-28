import asyncio

from agents.venue_agent import venue_agent


async def main():

    response = await venue_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": """
Find the best wedding venue
in Paris for 100 guests.
"""
                }
            ]
        }
    )

    print(response["structured_response"])


if __name__ == "__main__":
    asyncio.run(main())