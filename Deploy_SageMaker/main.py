import json
import requests

Test_example = { "data": "52, 1, 1, 128, 205, 1, 1, 184, 0, 0, 2, 0, 2" }
Appended_url = f'https://xoqrqtzsf4.execute-api.us-east-1.amazonaws.com/Alpha/sagemaker_api_resource'

response = requests.post(Appended_url, json=Test_example).json()
print(json.dumps(response, indent=4))