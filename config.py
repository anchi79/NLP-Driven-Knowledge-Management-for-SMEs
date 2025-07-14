import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "OpenAI Key Goes Here")
CRM_API_KEY = os.getenv("CRM_API_KEY", "CRM Key Goes Here")
USE_TTS = os.getenv("USE_TTS", "false").lower() == "false"

DATA_DIR = r"C:\Anand-mvp\data\docs"
TICKET_DB_PATH = os.path.join(DATA_DIR, "tickets.json")
