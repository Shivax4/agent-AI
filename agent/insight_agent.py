from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_insight_chain(llm):

    prompt = ChatPromptTemplate.from_template(
        """
Analyze the exit interview data below:

{data}

Provide:

1. Top reasons employees leave
2. Employee sentiment
3. Key improvement suggestions
"""
    )

    chain = prompt | llm | StrOutputParser()

    return chain