# Future AMD/LLM Integration

# from openai import OpenAI
#
# def generate_insights_llm(metrics, api_key):
#
#     client = OpenAI(api_key=api_key)
#
#     prompt = f"""
#     Convert metrics into executive insights:
#
#     {metrics}
#
#     Give:
#     - 3 insights
#     - 2 risks
#     - 3 recommendations
#     """
#
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#
#     return response.choices[0].message.content

def generate_insights(metrics):

    insights = [
        f"Total revenue reached ${metrics['total_revenue']:,}.",
        f"{metrics['top_region']} is the top-performing region.",
        f"Average churn is {metrics['avg_churn']}%."
    ]

    risks = [
        "Customer churn could impact future growth.",
        "Revenue concentration in one region may increase business risk."
    ]

    recommendations = [
        "Invest more in high-performing regions.",
        "Launch customer retention initiatives.",
        "Monitor KPIs monthly to sustain growth."
    ]

    return insights, risks, recommendations