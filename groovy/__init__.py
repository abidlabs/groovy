from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

def run(prompt: str):

    async def run_agent():
        agent = Agent(
            task=prompt,
            llm=ChatOpenAI(model="gpt-4o"),
        )
        result = await agent.run()
        return result

    return asyncio.run(run_agent())