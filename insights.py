import requests

def extract_sections(text):
    insights = []
    risks = []
    recommendations = []
    section = None

    for line in text.splitlines():
        line = line.strip()

        if line.upper().startswith("INSIGHTS"):
            section = "insights"
            continue

        if line.upper().startswith("RISKS"):
            section = "risks"
            continue

        if line.upper().startswith("RECOMMENDATIONS"):
            section = "recommendations"
            continue

        if line.startswith("-"):
            item = line[1:].strip()

            if section == "insights" and len(insights) < 3:
                insights.append(item)

            elif section == "risks" and len(risks) < 2:
                risks.append(item)

            elif section == "recommendations" and len(recommendations) < 3:
                recommendations.append(item)

    return insights, risks, recommendations


def generate_insights(metrics):
    prompt = f"""
You are a senior strategy consultant creating a boardroom-ready business review.

Business metrics:
Total revenue: ${metrics['total_revenue']:,}
Growth: {metrics['growth']}%
Top performing region: {metrics['top_region']}
Average churn: {metrics['avg_churn']}%

Return ONLY this format. Do not add extra sections or explanations.

INSIGHTS:
- ...
- ...
- ...

RISKS:
- ...
- ...

RECOMMENDATIONS:
- ...
- ...
- ...
"""

    response = requests.post(
        "http://localhost:8000/v1/chat/completions",
        json={
            "model": "Qwen/Qwen2-7B-Instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 350
        },
        timeout=120
    )

    response.raise_for_status()

    text = response.json()["choices"][0]["message"]["content"]

    insights, risks, recommendations = extract_sections(text)

    return insights, risks, recommendations




# ++from transformers import pipeline

# generator = None

# def get_generator():
#     global generator
#     if generator is None:
#         generator = pipeline(
#             "text-generation",
#             model="Qwen/Qwen2.5-3B-Instruct",
#             device_map="auto"
#         )
#     return generator

# def extract_sections(text):
#     # Keep only generated part after the LAST INSIGHTS:
#     if "INSIGHTS:" in text:
#         text = text[text.rfind("INSIGHTS:"):]

#     insights = []
#     risks = []
#     recommendations = []
#     section = None

#     for line in text.splitlines():
#         line = line.strip()

#         if line.startswith("INSIGHTS:"):
#             section = "insights"
#             continue
#         elif line.startswith("RISKS:"):
#             section = "risks"
#             continue
#         elif line.startswith("RECOMMENDATIONS:"):
#             section = "recommendations"
#             continue
#         elif line.startswith("---") or line.startswith("**Additional"):
#             break

#         if line.startswith("-"):
#             item = line[1:].strip()

#             if section == "insights" and len(insights) < 3:
#                 insights.append(item)
#             elif section == "risks" and len(risks) < 2:
#                 risks.append(item)
#             elif section == "recommendations" and len(recommendations) < 3:
#                 recommendations.append(item)

#     return insights, risks, recommendations


# def generate_insights(metrics):
#     model = get_generator()

#     prompt = f"""
# You are a senior business analyst.

# Business metrics:
# Total revenue: ${metrics['total_revenue']:,}
# Growth: {metrics['growth']}%
# Top region: {metrics['top_region']}
# Average churn: {metrics['avg_churn']}%

# Return ONLY the following format. Do not add extra sections or explanations.

# INSIGHTS:
# - ...
# - ...
# - ...

# RISKS:
# - ...
# - ...

# RECOMMENDATIONS:
# - ...
# - ...
# - ...
# """

#     response = model(
#         prompt,
#         max_new_tokens=180,
#         do_sample=False,
#         temperature=0.0
#     )

#     generated_text = response[0]["generated_text"]

#     insights, risks, recommendations = extract_sections(generated_text)

#     return insights, risks, recommendations


# Future AMD/LLM Integration

# from openai import OpenAI

# def generate_insights_llm(metrics, api_key):

#     client = OpenAI(api_key=api_key)

#     prompt = f"""
#     Convert metrics into executive insights:

#     {metrics}

#     Give:
#     - 3 insights
#     - 2 risks
#     - 3 recommendations
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )

#     return response.choices[0].message.content

# def generate_insights(metrics):

#     insights = [
#         f"Total revenue reached ${metrics['total_revenue']:,}.",
#         f"{metrics['top_region']} is the top-performing region.",
#         f"Average churn is {metrics['avg_churn']}%."
#     ]

#     risks = [
#         "Customer churn could impact future growth.",
#         "Revenue concentration in one region may increase business risk."
#     ]

#     recommendations = [
#         "Invest more in high-performing regions.",
#         "Launch customer retention initiatives.",
#         "Monitor KPIs monthly to sustain growth."
#     ]

#     return insights, risks, recommendations