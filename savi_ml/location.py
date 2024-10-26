import requests

# Define the API endpoint
url = "https://app.on-demand.io/rag-plugins/my-plugins"

# Include your API key and agent key in the headers
headers = {
    "Authorization": "Bearer sdtsHnRMzhRxzX9Wi7MsqAjhnQ6TocPr-",  # Your secret API key
    "Agent-Key": "plugin-1723275191",                          # Your agent key
    "Content-Type": "application/json"
}

try:
    # Make the API request
    response = requests.get(url, headers=headers)

    # Raise an error for bad responses (status codes 4xx and 5xx)
    response.raise_for_status()

    # Print the raw response text
    print("Raw Response:", response.text)

    # Attempt to parse and print the JSON response
    try:
        json_response = response.json()
        print("JSON Response:", json_response)
    except ValueError:
        print("Error parsing JSON response.")

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")  # Handle HTTP errors
except Exception as err:
    print(f"An error occurred: {err}")      # Handle other exceptions
