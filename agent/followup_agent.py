from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_followup_chain(llm):

    prompt = ChatPromptTemplate.from_template(
        """
You are assisting with an employee exit interview.

Employee response:
{answer}

If the response suggests issues related to salary, management,
workload, culture, or dissatisfaction, generate ONE short
follow-up question to better understand the issue.

If no follow-up is necessary, return exactly:

NONE

Return ONLY the question or NONE. Do not include explanations.
"""
    )

    chain = prompt | llm | StrOutputParser()

    return chain