import os
import uuid
from typing import Dict, Any, Callable
from langchain.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from pydantic import BaseModel

# Import tools dynamically
from tools.start_job import StartJobToolWrapper
from tools.weather_tool import WeatherTool  # Ensure you have WeatherTool properly implemented
from tools.circumference_tool import CircumferenceToolWrapper

# ✅ Set up the LLM Model
MODEL = "llama3.2"
llm = ChatOllama(model=MODEL)

# ✅ Register Multiple Tools
tool_registry = {
    "start_job": StartJobToolWrapper().get_tool(),
    "weather_tool": WeatherTool().get_tool(),
    "circuference_tool": CircumferenceToolWrapper().get_tool()
}


# ✅ Define the Generic State Manager
class StateManager(TypedDict):
    messages: Annotated[list, add_messages]
    extracted_value: str  # Generic field for job_id, city_name, etc.


# ✅ Generic Extraction Function
def extract_value(state: Dict[str, Any], extraction_type: str):
    """
    Extracts a specific value (e.g., job_id, city_name) from user input.

    :param state: The current workflow state
    :param extraction_type: The type of extraction (e.g., "job_id", "city_name")
    :return: Updated state with extracted value
    """
    user_input = state["messages"][-1].content

    res = llm.invoke(f"""
    You are given a question and need to extract a {extraction_type} from it.
    Respond ONLY with the extracted {extraction_type}. If none is found, return 'No answer provided'.

    Question:
    {user_input}
    """)

    extracted_value = res.content.strip()
    
    if extracted_value == "No answer provided":
        return {
            "messages": [AIMessage(content=f"I couldn't find a valid {extraction_type} in your question.")],
            "extracted_value": ""  
        }

    return {
        "messages": [AIMessage(content=f"Extracted {extraction_type}: {extracted_value}")],
        "extracted_value": extracted_value
    }


# ✅ Generic Tool Execution Function
def execute_tool(state: Dict[str, Any], tool_name: str):
    """
    Executes a registered tool using extracted input.

    :param state: The current workflow state
    :param tool_name: The name of the tool to execute (e.g., 'start_job', 'weather_tool')
    :return: Updated state with tool execution result
    """
    extracted_value = state.get("extracted_value", "").strip()

    if not extracted_value:
        return {
            "messages": [AIMessage(content=f"No valid input provided for {tool_name}. Cannot proceed.")]
        }

    tool = tool_registry.get(tool_name)
    if not tool:
        return {
            "messages": [AIMessage(content=f"Tool '{tool_name}' not found.")]
        }

    tool_result = tool.run(extracted_value)

    return {"messages": [AIMessage(content=tool_result)]}


# ✅ Workflow Orchestrator
class TaskOrchestrator:
    """
    A generic orchestrator to handle different task workflows using LangGraph.
    """

    def __init__(self, task_name: str, extraction_type: str):
        """
        Initializes the workflow for a specific task.

        :param task_name: The name of the task (e.g., "start_job", "weather_tool")
        :param extraction_type: The type of information to extract (e.g., "job_id", "city_name")
        """
        self.task_name = task_name
        self.extraction_type = extraction_type
        self.memory = MemorySaver()
        self.workflow = StateGraph(StateManager)

        # ✅ Add nodes dynamically
        self.workflow.add_node("extract", lambda state: extract_value(state, self.extraction_type))
        self.workflow.add_node("execute_tool", lambda state: execute_tool(state, self.task_name))

        # ✅ Define transitions dynamically
        self.workflow.add_edge(START, "extract")
        self.workflow.add_edge("extract", "execute_tool")
        self.workflow.add_edge("execute_tool", END)

        # ✅ Compile the workflow
        self.app = self.workflow.compile(checkpointer=self.memory)

    def run(self, user_input: str):
        """
        Runs the workflow for the given user input.
        """
        config = {"configurable": {"thread_id": str(uuid.uuid4())}}

        response = self.app.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config=config
        )

        return response["messages"][-1].content


# ✅ Example Usage: Running Both Workflows
if __name__ == "__main__":
    # ✅ Job Start Workflow
    job_orchestrator = TaskOrchestrator(task_name="start_job", extraction_type="job_id")
    user_query_job = "for job id aaaa1111 start the job"
    response_job = job_orchestrator.run(user_query_job)
    print("\nAI (Job):", response_job)

    # ✅ Weather Workflow
    weather_orchestrator = TaskOrchestrator(task_name="weather_tool", extraction_type="city_name")
    user_query_weather = "Tell me the weather for New York"
    response_weather = weather_orchestrator.run(user_query_weather)
    print("\nAI (Weather):", response_weather)

    # ✅ Weather Workflow
    circumference_orchestrator = TaskOrchestrator(task_name="circuference_tool", extraction_type="radius")
    user_query_circum = "calculate the circumference of a circle for the  radius 10.5"
    response_circum = circumference_orchestrator.run(user_query_circum)
    print("\nAI (circuferenc):", response_circum)

