from utils.llm import get_llm
from utils.prompts import DEBATER_B_PROMPT
from memory.vector_store import retrieve_memory

llm = get_llm()

def debater_b(state):

    short_history = state["history"][-1500:]
    past = retrieve_memory(state["topic"])
    past = str(past)[:700]

    prompt = DEBATER_B_PROMPT.format(
        topic=state["topic"],
        history=short_history + "\nRelevant past: " + past
    )

    response = llm.invoke(prompt).content.strip()

    state["history"] += f"\nB: {response}"
    return state
