from langchain.tools import Tool
from crm.client import CRMClient
from config import CRM_API_KEY

crm_client = CRMClient(api_key=CRM_API_KEY)


# Get recent tickets from CRM
def fetch_recent_tickets(query: str) -> str:
    tickets = crm_client.get_recent_tickets(query)
    if not tickets:
        return "No recent tickets found."
    summary = [f"Ticket #{t['id']}: {t['issue']} (Status: {t['status']})" for t in tickets]
    return "\n".join(summary)

ticket_tool = Tool(
    name="Ticket History Tool",
    func=fetch_recent_tickets,
    description="Retrieve the latest support tickets for a given customer ID."
)
