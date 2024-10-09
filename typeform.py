import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_typeform_responses(form_id):
    api_token = os.getenv('TYPEFORM_API_TOKEN')
    url = f"https://api.typeform.com/forms/{form_id}/responses"
    headers = {"Authorization": f"Bearer {api_token}"}
    params = {"page_size": 100}
    
    response = requests.get(url, headers=headers, params=params)
    
    print(response.json())

if __name__ == "__main__":
    form_id = os.getenv('TYPEFORM_FORM_ID')
    get_typeform_responses(form_id)