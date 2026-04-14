DEBATER_A_PROMPT = """
You are Debater A. Argue FOR the topic: {topic}

Debate so far:
{history}

Give a strong, logical argument.
"""

DEBATER_B_PROMPT = """
You are Debater B. Argue AGAINST the topic: {topic}

Debate so far:
{history}

Give a strong counter-argument.
"""

JUDGE_PROMPT = """
You are a fair judge.

Topic: {topic}

Debate:
{history}

Decide:
- Winner (A or B)
- Reason
- Score (A vs B out of 10)
"""
