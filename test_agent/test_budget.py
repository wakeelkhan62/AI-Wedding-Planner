import asyncio

from agents.budget_agent import budget_agent


async def main():

    response = await budget_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "My wedding budget is 50000."
                }
            ]
        }
    )

    print(response["structured_response"])


if __name__ == "__main__":
    asyncio.run(main())