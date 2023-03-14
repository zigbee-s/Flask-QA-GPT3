import os

class Config:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") 
    JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
    JIRA_API_KEY = os.environ.get("JIRA_API_KEY")