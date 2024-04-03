
import requests

class TranslationService:
    def __init__(self, endpoint, authorization_token):
        self.endpoint = endpoint
        self.headers = {
            'Authorization': f'Bearer {authorization_token}',
            'accept': 'application/json',
            'x-opera-timezone': 'Z',
            'Content-Type': 'application/json',
            'X-Opera-UI-Language': 'pl'
        }
        self.conversation_id = None

    def get_translation(self, selected_text: str) -> dict | int:
        payload = {
            'selected_text': selected_text
        }
        if self.conversation_id:
            payload['conversation_id'] = self.conversation_id

        response = requests.post(self.endpoint, headers=self.headers, json=payload)
        data = response.json()
        if response.status_code != 200:
            return response.status_code
        return data
    
