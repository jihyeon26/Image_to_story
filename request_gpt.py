import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Retrieve API key and endpoints from environment variables
GPT_ENDPOINT = os.getenv("GPT_ENDPOINT")
GPT_API_KEY = os.getenv("GPT_API_KEY")

def request_gpt(prompt, location, write_style, gender, companion):
    """
    Function to send a request to OpenAI GPT.

    Args:
        prompt (str): The prompt to be sent to the GPT model
        location (str): Location information to include in the travel record
        write_style (str): The writing style for the generated text
        gender (str): The user's gender

    Returns:
        str: Response from the GPT model
    """
    endpoint = GPT_ENDPOINT
    headers = {
        "Content-Type": "application/json",
        "api-key": GPT_API_KEY
    }
    payload = {
        "messages": [
            {
                "role": "system",
                "content": f"""
                    You are a writer who creates travel records. Take sentences and turn them into a travel record. 
                    Respond in English. Keep it under 800 characters.
                    I went near {location}. Limit the address to the city and region.
                    The {gender} in the photo is me.
                    I came on this trip with {companion}.
                    Respond in a {write_style} style.
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.1,
        "top_p": 0.4,
        "max_tokens": 800,
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        content = response_json["choices"][0]["message"]["content"]
        return content
    else:
        return f"{response.status_code}, {response.text}"
