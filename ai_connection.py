import requests

class AIConnection:
    def __init__(self):
        self.api_url = "https://api.example.com/ai"  # Replace with actual API URL
        self.api_key = "your_api_key"  # Replace with your actual API key

    def send_message(self, message):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "message": message
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get("response", "No response from AI")
        else:
            return "Error: Unable to get response from AI"