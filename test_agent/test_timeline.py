import asyncio

from agents.timeline_agent import timeline_agent


async def main():

    response = await timeline_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": """
Create a wedding timeline
starting at 6 PM.
"""
                }
            ]
        }
    )

    print(response["structured_response"])


if __name__ == "__main__":
    asyncio.run(main())