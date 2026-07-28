from langchain.tools import tool

from agents.venue_agent import venue_agent
from agents.budget_agent import budget_agent
from agents.catering_agent import catering_agent
from agents.decoration_agent import decoration_agent
from agents.timeline_agent import timeline_agent


config = {
    "configurable": {
        "thread_id": "streamlit-user-1"
    }
}


@tool
async def call_venue_agent(query: str):
    """
    Delegate venue-related tasks to the Venue Agent.
    """

    prompt = f"""
User Request:

{query}

Use previous wedding information if available.

Only answer venue related questions.
"""

    response = await venue_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        config=config
    )

    return response["structured_response"]


@tool
async def call_budget_agent(query: str):
    """
    Delegate budget planning to the Budget Agent.
    """

    prompt = f"""
User Request:

{query}

Use previous wedding information if available.

Only answer budget related questions.
"""

    response = await budget_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        config=config
    )

    return response["structured_response"]


@tool
async def call_catering_agent(query: str):
    """
    Delegate catering planning to the Catering Agent.
    """

    prompt = f"""
User Request:

{query}

Use previous wedding information if available.

Only answer catering related questions.
"""

    response = await catering_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        config=config
    )

    return response["structured_response"]


@tool
async def call_decoration_agent(query: str):
    """
    Delegate decoration planning to the Decoration Agent.
    """

    prompt = f"""
User Request:

{query}

Use previous wedding information if available.

Only answer decoration related questions.
"""

    response = await decoration_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        config=config
    )

    return response["structured_response"]


@tool
async def call_timeline_agent(query: str):
    """
    Delegate timeline planning to the Timeline Agent.
    """

    prompt = f"""
User Request:

{query}

Use previous wedding information if available.

Only answer timeline related questions.
"""

    response = await timeline_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        config=config
    )

    return response["structured_response"] 