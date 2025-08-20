import requests

def fetch_user(user_id):
    """模擬呼叫外部 API"""
    response = requests.get(f"http://example.com/users/{user_id}")
    return response.json()
