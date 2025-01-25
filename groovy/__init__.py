from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

def run(prompt: str):
    agent = Agent(
        task=prompt,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())