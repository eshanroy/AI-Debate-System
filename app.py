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

topic = st.text_input(
    "🎯 Enter Debate Topic",
    placeholder="Example: Magnus Carlsen is the best chess player"
)

if st.button("Start Debate", type="primary"):
    if not topic.strip():
        st.warning("Please enter a debate topic.")
    else:
        state = {
            "topic": topic.strip(),
            "history": "",
            "result": "",
            "round_arguments": {},
            "current_round": 1
        }

        rounds = 3

        st.subheader(f"🎯 Topic: {topic.strip()}")
        st.markdown("---")

        try:
            for i in range(rounds):
                round_number = i + 1
                state["current_round"] = round_number

                st.subheader(f"🔁 Round {round_number}")

                with st.spinner(
                    f"Debater A is preparing Round {round_number}..."
                ):
                    state = debater_a(state)

                last_a = state["round_arguments"][round_number]["A"]

                st.markdown("**🅰️ Debater A**")
                st.markdown(last_a)

                with st.spinner(
                    f"Debater B is preparing Round {round_number}..."
                ):
                    state = debater_b(state)

                last_b = state["round_arguments"][round_number]["B"]

                st.markdown("**🅱️ Debater B**")
                st.markdown(last_b)

                st.markdown("---")

            st.subheader("⚖️ Final Judgment")

            with st.spinner("The judge is evaluating the debate..."):
                state = judge(state)

            st.markdown(
                state.get("result", "The judge did not return a verdict.")
            )

            st.success("Debate completed successfully!")

        except Exception as e:
            st.error("The debate stopped because an agent or the judge failed.")
            st.exception(e)
