from dotenv import load_dotenv
from langchain_groq import ChatGroq

from agents.followup_agent import create_followup_chain
from agents.structuring_agent import create_structuring_chain
from agents.insight_agent import create_insight_chain

from workflow.controller import run_interview

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

followup_chain = create_followup_chain(llm)

structuring_chain = create_structuring_chain(llm)

insight_chain = create_insight_chain(llm)

run_interview(
    followup_chain,
    structuring_chain,
    insight_chain
)