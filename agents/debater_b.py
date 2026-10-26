
from utils.llm import get_llm
from utils.prompts import DEBATER_B_PROMPT
from memory.vector_store import retrieve_memory

llm = get_llm()


def debater_b(state):
    short_history = state.get("history", "")[-1500:]

    past = retrieve_memory(state["topic"])
    past = str(past)[:700]

    prompt = DEBATER_B_PROMPT.format(
        topic=state["topic"],
        history=short_history + "\nRelevant past: " + past
    )

    response = llm.invoke(prompt).content

    if not isinstance(response, str):
        response = str(response)

    response = response.strip()

    if not response:
        raise ValueError("Debater B returned an empty response.")

    state["round_arguments"] = state.get("round_arguments", {})
    round_number = state.get("current_round", 1)

    state["round_arguments"].setdefault(round_number, {})
    state["round_arguments"][round_number]["B"] = response

    state["history"] = (
        state.get("history", "")
        + f"\n\nRound {round_number} - B: {response}"
    )

    return state
