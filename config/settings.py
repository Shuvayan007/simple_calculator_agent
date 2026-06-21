from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "endpoint" : os.getenv("AZURE_OPENAI_ENDPOINT"),
    "api_key" : os.getenv("AZURE_OPENAI_API_KEY"),
    "deployment_name" : os.getenv("AZURE_DEPLOYMENT_NAME")
}