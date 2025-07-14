class CRMClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_customer_info(self, customer_id: str) -> str:
        return f"Customer Info for {customer_id}: Name: Anand Kumar, Email: s_anchi@yahoo.co.in"

    def get_recent_tickets(self, customer_id: str, limit: int = 3) -> list:
        return [
            {"id": 1, "issue": "Login not working", "status": "Resolved"},
            {"id": 2, "issue": "Payment issue", "status": "Pending"},
            {"id": 3, "issue": "Update account info", "status": "Resolved"},
            {"id": 105, "issue": "Parking access card malfunction", "status": "Pending"},
            {"id": 104, "issue": "Air-conditioning not cooling in master bedroom", "status": "Resolved"},
            {"id": 103, "issue": "Annual lease-renewal terms clarification", "status": "Resolved"},
            {"id": 102, "issue": "Minor water leakage from bathroom ceiling", "status": "Resolved"},
            {"id": 101, "issue": "Dispute over late-payment notice (auto-debit failed)", "status": "Closed"},
        ]

    def get_related_KMS(self, customer_id: str, limit: int = 3) -> list:
        return [
            {"id": 1, "policy": "Return policy", "status": "Related"},
            {"id": 2, "policy": "Payment terms", "status": "Related"},
            {"id": 3, "Procedure": "Rent process", "status": "Related"},
            {"id": 301, "policy": "Parking access control & card replacement", "status": "Related"},
            {"id": 302, "procedure": "Split-unit AC maintenance troubleshooting guide", "status": "Related"},
            {"id": 303, "policy": "Residential lease-renewal process & timelines", "status": "Related"},
            {"id": 304, "procedure": "Emergency plumbing & leak containment steps", "status": "Related"},
            {"id": 305, "policy": "Late-payment charges & dispute resolution", "status": "Related"},
        ]
