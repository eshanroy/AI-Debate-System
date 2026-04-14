import os
import streamlit as st
from agents.debater_a import debater_a
from agents.debater_b import debater_b
from agents.judge import judge

st.set_page_config(page_title="AI Debate System", layout="centered")

st.title("🧠 AI Debate System")
st.write("Multi-Agent Debate with Memory (Groq + LangChain)")

# Input
topic = st.text_input("🎯 Enter Debate Topic")

if st.button("Start Debate") and topic:

    state = {
        "topic": topic,
        "history": "",
        "result": ""
    }

    rounds = 3

    st.subheader(f"🎯 Topic: {topic}")
    st.markdown("---")

    # 🔁 Debate rounds
    for i in range(rounds):
        st.subheader(f"🔁 Round {i+1}")

        # Debater A
        state = debater_a(state)
        last_a = state["history"].split("A:")[-1].strip()

        st.text_area(
            "🅰️ Debater A",
            value=last_a,
            height=150
        )

        # Debater B
        state = debater_b(state)
        last_b = state["history"].split("B:")[-1].strip()

        st.text_area(
            "🅱️ Debater B",
            value=last_b,
            height=150
        )

        st.markdown("---")

    # ⚖️ Final Judgment
    st.subheader("⚖️ Final Judgment")

    state = judge(state)

    st.text_area(
        "📜 Judge Decision",
        value=state["result"],
        height=300
    )