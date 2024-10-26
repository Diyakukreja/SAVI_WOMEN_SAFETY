import requests

# Replace with your actual API key and external user ID
api_key = "bbqiaLOgHI3HrofA0RAXP3JB0u4Nao6q"
external_user_id = "test1"

# Step 1: Create Chat Session
create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
headers = {
    'apikey': api_key
}
create_session_body = {
    "pluginIds": [],
    "externalUserId": external_user_id
}

response = requests.post(create_session_url, headers=headers, json=create_session_body)
response_data = response.json()

# Extract session ID from the response
session_id = response_data['data']['id']

# Step 2: Submit Query
submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
submit_query_body = {
    "endpointId": "predefined-openai-gpt4o",
    "query": "Hi, my name is Diya",
    "pluginIds": ["plugin-1723275191", "plugin-1726226353", "plugin-1717459265"],
    "responseMode": "sync"
}

query_response = requests.post(submit_query_url, headers=headers, json=submit_query_body)
query_response_data = query_response.json()

# Print the response from the query submission
print(query_response_data["data"]["answer"])
