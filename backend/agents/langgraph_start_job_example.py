from langchain_openai import ChatOpenAI
from langchain_community.utilities import OpenWeatherMapAPIWrapper
import os
import uuid
from langchain.tools import Tool
from langchain.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from pydantic import BaseModel  # Required for StructuredTool


from tools.start_job import StartJobToolWrapper

cir = StartJobToolWrapper().get_tool()

# Define LLM Model
MODEL = "llama3.2"
llm = ChatOllama(model=MODEL)


def agent(state):
    user_input = state["messages"][-1].content  # Extract the latest user message
    
    res = llm.invoke(f"""
    You are given one question and you have to extract the job_id from it.
    Respond ONLY with the job_id. If you cannot find a job_id, respond with an empty string.

    Here is the question:
    {user_input}
    """)

    job_id = res.content.strip()
    
    if not job_id:
        return {
            "messages": [AIMessage(content="I couldn't find a job_id in your question.")],
            "job_id": ""  # ✅ Ensure job_id is in the state, even if empty
        }

    return {
        "messages": [AIMessage(content=f"Extracted number: {job_id}")],
        "job_id": job_id  # ✅ Store correctly for the next function
    }

# **Node 2: Fetch weather information**
def start_my_job(state):
    job_id = state.get("job_id", "").strip()  # ✅ Use `job_id`, not `number`

    if not job_id:
        return {
            "messages": [AIMessage(content="No job_id provided. Cannot start job.")]
        }

    job_info = cir.run(job_id)  # ✅ Start job with correct job_id
    return {"messages": [AIMessage(content=job_info)]}


# **Define the State**
# ✅ Use 'job_id' instead of 'number' to maintain state correctly
class State(TypedDict):
    messages: Annotated[list, add_messages]
    job_id: str  # ✅ Ensuring job_id persists in state


# **Setup Workflow**
memory = MemorySaver()
workflow = StateGraph(State)

# **Define Transitions Between Nodes**
# ✅ Fix incorrect transition names and ensure 'job_id' is passed properly
workflow.add_edge(START, "agent")
workflow.add_node("agent", agent)
workflow.add_node("start_my_job", start_my_job)  # ✅ Corrected node name

workflow.add_edge("agent", "start_my_job")  # ✅ Ensure agent passes job_id correctly
workflow.add_edge("start_my_job", END)  # ✅ Final transition


# **Compile Workflow with Memory Checkpointer**
app = workflow.compile(checkpointer=memory)

# **Create a unique config dictionary to satisfy the checkpointer requirements**
config = {"configurable": {"thread_id": str(uuid.uuid4())}}

# **Run the Workflow**
user_query = "for job id aaaa1111 start the job"
response = app.invoke({"messages": [HumanMessage(content=user_query)]}, config=config)

# **Print Response**
print("AI:", response["messages"][-1].content)