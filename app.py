import os
from typing import Annotated

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
import gradio as gr


_api_key = os.getenv("OPENAI_API_KEY")
if not _api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY environment variable is not set. "
        "Please export it before running this application."
    )
os.environ["OPENAI_API_KEY"] = _api_key

llm = ChatOpenAI(model_name="gpt-4o-mini")


# ---------------------------------------------------------------------------
# LangGraph state definition
# ---------------------------------------------------------------------------

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# ---------------------------------------------------------------------------
# Graph nodes
# ---------------------------------------------------------------------------

def chatbot_node(state: State) -> State:
    """Invoke the LLM with the current conversation and return the reply."""
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


# ---------------------------------------------------------------------------
# Build the graph
# ---------------------------------------------------------------------------

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()


# ---------------------------------------------------------------------------
# Gradio chat interface
# ---------------------------------------------------------------------------

def chat(user_message: str, history: list[list[str]]) -> str:
    """Convert Gradio history to LangChain messages and run the graph."""
    messages: list[BaseMessage] = []
    for human, assistant in history:
        messages.append(HumanMessage(content=human))
        messages.append(AIMessage(content=assistant))
    messages.append(HumanMessage(content=user_message))

    result = graph.invoke({"messages": messages})
    return result["messages"][-1].content


iface = gr.ChatInterface(
    fn=chat,
    title="LangGraph Chatbot",
    description="A conversational chatbot built with LangGraph and OpenAI GPT-4o-mini.",
    examples=["Hello! Who are you?", "Tell me a joke.", "What is LangGraph?"],
)

iface.launch()

