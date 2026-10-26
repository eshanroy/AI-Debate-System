import os
import streamlit as st

from agents.debater_a import debater_a
from agents.debater_b import debater_b
from agents.judge import judge

st.set_page_config(
    page_title="AI Debate System",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Debate System")
st.write("Multi-Agent Debate with Memory (Groq + LangChain)")

# Debate topic input
topic = st.text_input(
    "🎯 Enter Debate Topic",
    placeholder="Example: Magnus Carlsen is the best chess player"
)

# Start debate
if st.button("Start Debate", type="primary"):

    if not topic.strip():
        st.warning("Please enter a debate topic before starting.")
    else:
        state = {
            "topic": topic.strip(),
            "history": "",
            "result": ""
        }

        rounds = 3

        st.subheader(f"🎯 Topic: {topic.strip()}")
        st.markdown("---")

        try:
            # Run the debate
            for i in range(rounds):
                round_number = i + 1

                st.subheader(f"🔁 Round {round_number}")

                # Debater A
                with st.spinner(
                    f"Debater A is preparing Round {round_number}..."
                ):
                    state = debater_a(state)

                history_after_a = state.get("history", "")
                last_a = history_after_a.split("A:")[-1].strip()

                st.text_area(
                    "🅰️ Debater A",
                    value=last_a,
                    height=150,
                    key=f"debater_a_output_{round_number}",
                    disabled=True
                )

                # Debater B
                with st.spinner(
                    f"Debater B is preparing Round {round_number}..."
                ):
                    state = debater_b(state)

                history_after_b = state.get("history", "")
                last_b = history_after_b.split("B:")[-1].strip()

                st.text_area(
                    "🅱️ Debater B",
                    value=last_b,
                    height=150,
                    key=f"debater_b_output_{round_number}",
                    disabled=True
                )

                st.markdown("---")

            # Final judgment
            st.subheader("⚖️ Final Judgment")

            with st.spinner("The judge is evaluating the debate..."):
                state = judge(state)

            st.text_area(
                "📜 Judge Decision",
                value=state.get("result", "No decision was returned."),
                height=300,
                key="judge_decision_output",
                disabled=True
            )

            st.success("Debate completed successfully!")

        except Exception as e:
            st.error(
                "The debate could not be completed. "
                "Check the Render logs for the underlying error."
            )
            st.exception(e)
