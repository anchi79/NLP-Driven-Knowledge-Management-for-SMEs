from langchain.tools import Tool
from crm.client import CRMClient
from config import CRM_API_KEY

crm_client = CRMClient(api_key=CRM_API_KEY)

def fetch_customer_info(query: str) -> str:
    return crm_client.get_customer_info(query)

# When the API is provided , it should be used here
crm_tool = Tool(
    name="CRM Info Tool",
    func=fetch_customer_info,
    description="Use this tool to get customer information from CRM by customer ID."
)
