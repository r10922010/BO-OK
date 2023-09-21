import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT = os.getenv("gmail_account")
PASSWORD = os.getenv("gmail_password")