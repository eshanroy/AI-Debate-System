from agents.debater_a import debater_a
from agents.debater_b import debater_b
from agents.judge import judge
from speech.text_to_speech import speak   # optional (kept safe)


def run():

    # ✅ Text-only input (voice removed)
    topic = input("Enter topic: ")

    state = {
        "topic": topic,
        "history": "",
        "result": ""
    }

    rounds = 3

    print("\n==============================")
    print(f"🎯 Debate Topic: {topic}")
    print("==============================\n")

    # 🔁 Debate rounds
    for i in range(rounds):
        print(f"\n🔁 ROUND {i+1}")

        state = debater_a(state)
        state = debater_b(state)

    # ⚖️ Final judgment
    print("\n⚖️ FINAL JUDGMENT")
    state = judge(state)

    print("\n===== FINAL RESULT =====")
    print(state["result"])

    # 🔊 Optional speech output (safe fallback)
    speak(state["result"])


if __name__ == "__main__":
    run()