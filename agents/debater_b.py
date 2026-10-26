from utils.llm import get_llm
from utils.prompts import DEBATER_B_PROMPT
from memory.vector_store import retrieve_memory

llm = get_llm()


def extract_response_content(message):
    """Extract text from a LangChain AIMessage response."""
    content = message.content

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, str):
                text_parts.append(block)
            elif isinstance(block, dict):
                text = block.get("text", "")
                if text:
                    text_parts.append(text)

        return "\n".join(text_parts).strip()

    return str(content).strip() if content else ""


def debater_b(state):
    short_history = state.get("history", "")[-1500:]

    past = retrieve_memory(state["topic"])
    past = str(past)[:700]

    prompt = DEBATER_B_PROMPT.format(
        topic=state["topic"],
        history=short_history + "\nRelevant past: " + past
    )

    # Retry once if the model returns an empty response.
    response = ""

    for attempt in range(2):
        current_prompt = prompt

        if attempt == 1:
            current_prompt += (
                "\n\nIMPORTANT: Provide a complete, substantive "
                "counterargument to Debater A. Respond with plain text. "
                "Do not return an empty response."
            )

        message = llm.invoke(current_prompt)
        response = extract_response_content(message)

        if response:
            break

    if not response:
        raise ValueError(
            "Debater B returned an empty response after two attempts. "
            "Check the Render logs and Groq model availability."
        )

    round_number = state.get("current_round", 1)

    state.setdefault("round_arguments", {})
    state["round_arguments"].setdefault(round_number, {})
    state["round_arguments"][round_number]["B"] = response

    state["history"] = (
        state.get("history", "")
        + f"\n\nRound {round_number} - B: {response}"
    )

    return state
