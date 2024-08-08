import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8000/get"

# Your credentials
username = 'admin'
password = 1111

token = '780cf90fcebe0fd431a2f9e704cc30a123b71bbd'
# bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMTQyMDA0LCJpYXQiOjE3MjMxMDk2MDQsImp0aSI6ImY2ZWIwZTMxYjI0MjRkZjFiMjg4Y2NiMGIxN2NiZDQ3IiwidXNlcl9pZCI6MX0.ruhlBfqYQdYSXuZ9tTbx5OxxeK5a_tsTz0B6EIiU8KM"

# Headers with Bearer token
headers = {
    # 'Authorization': f'Bearer {bearer_token}',
    'Authorization': f'token {token}',
}

# Make a GET request with Basic Authentication
# response = requests.get(url, auth=HTTPBasicAuth(username, password))



# Make a GET request with Bearer Token Authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)


# Check the response status
if response.status_code == 200:
    # Success: process the response data
    print('Response:', response.json())
else:
    # Error: print the status code and message
    print(f'Error: {response.status_code} - {response.text}')
