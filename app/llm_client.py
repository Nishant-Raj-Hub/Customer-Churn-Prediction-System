import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_actions(risk, prob, drivers):
    prompt = f"""
You are a senior customer retention strategist.

Customer churn risk level: {risk}
Churn probability: {prob}

Key churn drivers:
{drivers}

Respond strictly in this format:

WHY (1 to 2 sentences explaining the churn risk based on the drivers):
<short explanation>

ACTIONS: 
- action 1 (10 to 15 words)
- action 2 (10 to 15 words)
- action 3 (10 to 15 words)
- action 4 (10 to 15 words)
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You give practical, business-focused advice."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=400
    )

    text = response.choices[0].message.content.strip()

    why_part, actions_part = text.split("ACTIONS:")
    explanation = why_part.replace("WHY:", "").strip()
    actions = [
        a.strip("- ").strip()
        for a in actions_part.split("\n")
        if a.strip()
    ]

    return explanation, actions






















# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_actions(churn_risk, churn_prob, drivers):
#     """
#     Uses LLM to explain churn risk and recommend actions.
#     ML decides risk & drivers. LLM only explains.
#     """

#     prompt = f"""
# You are a customer retention expert working for a telecom company.

# Context:
# - Churn risk level: {churn_risk}
# - Churn probability: {int(churn_prob * 100)}%
# - Key churn drivers:
# {', '.join(drivers)}

# Rules:
# - Do NOT invent new reasons.
# - Do NOT contradict the churn drivers.
# - Keep suggestions realistic for a telecom business.
# - Be concise and actionable.

# Tasks:
# 1. Explain in simple business terms why this customer may churn.
# 2. Suggest 3 concrete actions to reduce churn.
# """

#     response = client.chat.completions.create(
#         model="gpt-3.5",
#         messages=[
#             {"role": "system", "content": "You are a helpful business analyst."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3
#     )

#     text = response.choices[0].message.content.strip()

#     # Split explanation and actions cleanly
#     lines = text.split("\n")

#     explanation = []
#     actions = []

#     section = "explanation"
#     for line in lines:
#         if "action" in line.lower():
#             section = "actions"
#             continue
#         if section == "explanation":
#             explanation.append(line)
#         else:
#             if line.strip():
#                 actions.append(line.strip("-• "))

#     return "\n".join(explanation), actions[:3]
