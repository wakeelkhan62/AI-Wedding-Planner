import asyncio

from agents.coordinator import coordinator
from config.logger import logger


async def main():

    print("=" * 60)
    print("🤖 AI Wedding Planner")
    print("=" * 60)

    # Memory Configuration
    config = {
        "configurable": {
            "thread_id": "wedding-session-1"
        }
    }

    logger.info("AI Wedding Planner Started")

    while True:

        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            logger.info("Application Closed")
            print("\n👋 Goodbye!")
            break

        logger.info(f"User Query: {query}")

        try:

            response = await coordinator.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": query,
                        }
                    ]
                },
                config=config,
            )

            logger.info("Coordinator Response Generated")

            print("\n" + "=" * 60)
            print("📋 Wedding Planning Session")
            print("=" * 60)
            print(f"📝 User Request: {query}")
            print("-" * 60)
            print("🤖 Wedding Planner")
            print("-" * 60)
            print(response["messages"][-1].content)
            print("=" * 60)

        except Exception as e:

            logger.error(str(e))

            print("\n Something went wrong!")
            print(e)


if __name__ == "__main__":
    asyncio.run(main())