from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from prompt import planner_prompt
from states import Plan, File
from langgraph.graph import StateGraph,START,END
from typing import Annotated, Sequence
from typing import TypedDict
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph.message import add_messages

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
llm=ChatGroq(model="openai/gpt-oss-120b")


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def planner_agent(state):
    print("Messages in AgentState:", state["messages"])
    user_prompt = state["messages"][-1].content  # last message text
    resp = llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    print("LLM Response:", resp)
    return {"messages": [HumanMessage(content=str(resp))]}


graph = StateGraph(AgentState)
graph.add_node("planner", planner_agent)
graph.add_edge(START, "planner")
graph.add_edge("planner", END)
builder=graph.compile()


user_question = "Create a calculator web application?"
input_state = {
    "messages": [HumanMessage(content=user_question)]
}

builder.invoke(input_state)