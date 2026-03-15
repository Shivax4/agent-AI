from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_structuring_chain(llm):

    prompt = ChatPromptTemplate.from_template(
        """
Convert this exit interview conversation into structured JSON.

Conversation:
{conversation}

Extract fields:

reason_for_leaving
overall_experience
liked_most
improvement_suggestions
manager_relationship
recommendation
"""
    )

    chain = prompt | llm | StrOutputParser()

    return chain