from langchain_openai import AzureChatOpenAI
from config.settings import CONFIG

# print(CONFIG["endpoint"])
# print(CONFIG["deployment_name"])

llm = AzureChatOpenAI(
    api_key= CONFIG["api_key"],
    azure_endpoint= CONFIG["endpoint"],
    azure_deployment= CONFIG["deployment_name"],
    api_version=''
)

# print(llm)