
import os
import requests
from config import Config

def prompt_watsonx(prompt_text):
    if Config.USE_MOCK_AI:
        return "Using local logistics recommendation engine. (AI Service Unavailable)"
        
    url = f"{Config.WATSONX_URL}/ml/v1-beta/generation/text?version=2023-05-29"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Config.WATSONX_API_KEY}"
    }
    body = {
        "model_id": "ibm/granite-13b-chat-v2",
        "input": prompt_text,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200
        },
        "project_id": Config.WATSONX_PROJECT_ID
    }
    
    try:
        response = requests.post(url, headers=headers, json=body, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["results"][0]["generated_text"]
    except Exception as e:
        print("Watsonx failed:", e)
        return "AI service unavailable. Using local logistics recommendation engine."
