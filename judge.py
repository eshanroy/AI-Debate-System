from utils.llm import get_llm
from utils.prompts import JUDGE_PROMPT
from memory.vector_store import store_memory

llm = get_llm()

def judge(state):

    short_history = state["history"][-2000:]  # slightly more

    prompt = JUDGE_PROMPT.format(
        topic=state["topic"],
        history=short_history
    )

    result = llm.invoke(prompt).content.strip()

    state["result"] = result

    store_memory(state["topic"] + "\n" + short_history + "\n" + result)

    return state