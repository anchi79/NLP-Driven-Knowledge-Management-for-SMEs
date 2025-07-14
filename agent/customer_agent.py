import sys
sys.path.append('../')
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from tools.crm_tool import crm_tool
from tools.ticket_tool import ticket_tool
from memory.vector_store import load_company_docs
from config import OPENAI_API_KEY

# from langchain.chat_models import ChatOpenAI


def create_agent():
    llm = OpenAI(temperature=0)
    tools = [crm_tool, ticket_tool]

    # Load company documentation as a retriever tool with source attribution
    retriever = load_company_docs().as_retriever()
    qa_tool = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, retriever=retriever)

    def run_with_sources(query: str) -> str:
        result = qa_tool({"question": query})
        answer = result.get("answer", "No records found")
        sources = result.get("sources", "")
        return f"{answer}\n\nSources: {sources}" if sources else answer

    docs_tool = Tool(
        name="CompanyDocs",
        func=run_with_sources,
        description="Documents that contain company's data"
    )

    tools.append(docs_tool)


    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type="zero-shot-react-description",
        verbose=True
    )
    return agent
