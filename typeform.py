import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_typeform_responses(form_id):
    api_token = os.getenv('TYPEFORM_API_TOKEN')
    url = f"https://api.typeform.com/forms/{form_id}/responses"
    headers = {"Authorization": f"Bearer {api_token}"}
    params = {"page_size": 100}
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def process_responses(responses):
    # Extract relevant data from responses
    processed_data = []
    for item in responses['items']:
        answer_dict = {}
        for answer in item['answers']:
            question_id = answer['field']['id']
            answer_dict[question_id] = answer.get('text') or answer.get('choice', {}).get('label') or answer.get('number')
        
        answer_dict['submitted_at'] = item['submitted_at']
        processed_data.append(answer_dict)
    
    return processed_data

def save_to_csv(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    form_id = os.getenv('TYPEFORM_FORM_ID')
    responses = get_typeform_responses(form_id)
    processed_data = process_responses(responses)
    save_to_csv(processed_data, 'typeform_responses.csv')