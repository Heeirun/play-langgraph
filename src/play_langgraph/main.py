import getpass
import os
from dotenv import load_dotenv
from play_langgraph.state import State  # This will work after installing with -e
from langgraph.graph import StateGraph, START, END, Graph
from langchain_anthropic import ChatAnthropic
from IPython.display import Image, display

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-haiku-20241022")

def _set_env(var: str):
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        api_key = getpass.getpass(f"{var}: ")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

def stream_graph_updates(user_input: str, graph: Graph):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

def main():
    print("Hello from play-langgraph!")
    _set_env("ANTHROPIC_API_KEY")
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    graph = graph_builder.compile()

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input, graph)
        except:
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(user_input, graph)
            break

if __name__ == "__main__":
    main()
