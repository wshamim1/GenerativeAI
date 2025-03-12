import asyncio
import sys, os
# Ensure the backend directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))



from backend.agents.agent_executor import AgentExecutor

async def main():
    tool_class_names = ['WikiTool', 'WeatherTool']
    agent_executor = await AgentExecutor.create(llm_name='ollama', model_name='llama3.2', tool_class_names=tool_class_names)

    response = await agent_executor.run("tell me about pele and then tell me the weather for New York.")
    print(response)

# Ensure proper asyncio execution
if __name__ == "__main__":
    asyncio.run(main())


