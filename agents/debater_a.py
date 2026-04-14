from utils.llm import get_llm
from utils.prompts import DEBATER_A_PROMPT
from memory.vector_store import retrieve_memory

llm = get_llm()

def debater_a(state):

    short_history = state["history"][-1500:]
    past = retrieve_memory(state["topic"])
    past = str(past)[:700]

    prompt = DEBATER_A_PROMPT.format(
        topic=state["topic"],
        history=short_history + "\nRelevant past: " + past
    )

    response = llm.invoke(prompt).content.strip()

    state["history"] += f"\nA: {response}"
    return state
