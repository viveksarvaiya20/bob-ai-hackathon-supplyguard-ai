import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
    WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
    WATSONX_URL = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
    
    CLOUDANT_URL = os.getenv("CLOUDANT_URL")
    CLOUDANT_API_KEY = os.getenv("CLOUDANT_API_KEY")
    
    # Flags for mock data if cloudant/watsonx fail
    USE_MOCK_DB = not bool(CLOUDANT_URL and CLOUDANT_API_KEY)
    USE_MOCK_AI = not bool(WATSONX_API_KEY and WATSONX_PROJECT_ID)
