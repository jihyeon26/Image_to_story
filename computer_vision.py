import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key and endpoints from environment variables
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")
VISION_KEY = os.getenv("VISION_KEY")


def request_vision(image_path):
    endpoint = VISION_ENDPOINT
    
    params = {
        "api-version" :"2024-02-01",
        "language":"en",
        "features": "denseCaptions",
    }
    headers = {
        "ocp-apim-subscription-key" : VISION_KEY,
        "Content-Type": "application/octet-stream"
    }
    
    with open(image_path, "rb") as image:
        image_data = image.read()
        
    response = requests.post(endpoint, params=params, headers=headers, data = image_data)
    captions = []
    if response.status_code == 200:
        response_json = response.json()
        values = response_json['denseCaptionsResult']['values']
        for value in values:
            text = value["text"]
            captions.append(text)
        prompt = "\n".join(captions)
        return prompt
    else:
        return dict(status=response.status_code, message=response.text)

# print(request_vision(r"C:\Users\USER\Documents\ms_2차 프로젝트\images\20240611_120530.jpg"))