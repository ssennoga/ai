from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.config import LLM_MODEL, TEMPERATURE

def create_simple_rag_agent():
    """
    Very simple simulated RAG agent — replace with real retriever + LLM chain
    """
    llm = ChatOpenAI(model=LLM_MODEL, temperature=TEMPERATURE)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful and accurate assistant."),
        ("user", "{question}")
    ])

    chain = prompt | llm | StrOutputParser()
    return chain