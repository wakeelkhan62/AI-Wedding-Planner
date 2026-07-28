import asyncio

from agents.coordinator import coordinator


async def main():

    response = await coordinator.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Plan my complete wedding in Paris for 100 guests with a budget of $50,000."
                }
            ]
        }
    )

    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())