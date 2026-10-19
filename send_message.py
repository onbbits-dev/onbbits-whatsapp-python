"""
OnBBits Python Integration - Send WhatsApp Message Example

This script demonstrates how to send a WhatsApp message using the OnBBits
API Campaign endpoint with Python and the `requests` library.

Note: This is an integration example, not an official Python SDK.
"""

import json
import requests


# ==============================================================================
# Configuration
# Replace the placeholder values below with your OnBBits API Campaign details.
# You can find your API token and campaign details in your OnBBits dashboard.
# ==============================================================================

# Default OnBBits API Campaign endpoint
API_CAMPAIGN_URL = "https://api.onbbits.io/api/campaigns/send"

# Your OnBBits API token / key
API_KEY = "YOUR_ONBBITS_API_TOKEN"

# OnBBits API Campaign payload
# Note: OnBBits expects the authentication token inside the request body ("token"),
# not as an Authorization HTTP header.
PAYLOAD = {
    "token": API_KEY,
    "campaignName": "YOUR_CAMPAIGN_NAME",
    "destination": "+91 98765 43210",  # Recipient phone number with country code (e.g. +91...)
    "userName": "Recipient Name",
    "components": [
        {
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": "Hello from OnBBits Python integration!"
                }
            ]
        }
    ]
}


def send_whatsapp_message(api_url, api_key, payload):
    """
    Send a WhatsApp message via an OnBBits API Campaign endpoint.

    :param api_url: The OnBBits API Campaign endpoint URL (e.g. 'https://api.onbbits.io/api/campaigns/send').
    :param api_key: Your OnBBits API Token (passed in request body as 'token').
    :param payload: The JSON request payload containing campaignName, destination, userName, and components.
    :return: The API response as a Python dictionary if successful, None otherwise.
    """
    # Clone payload and ensure token is set in request body
    request_payload = dict(payload)
    if api_key and (
        "token" not in request_payload
        or request_payload["token"] == "YOUR_ONBBITS_API_TOKEN"
    ):
        request_payload["token"] = api_key

    # Validate configuration placeholders
    if (
        api_key == "YOUR_ONBBITS_API_TOKEN"
        or request_payload.get("token") == "YOUR_ONBBITS_API_TOKEN"
        or request_payload.get("destination") == "+91 98765 43210"
    ):
        print(
            "[Configuration Warning] Please replace 'API_KEY', 'destination', "
            "and other placeholder values in 'send_message.py' with your actual OnBBits details."
        )
        return None

    # OnBBits API Campaign requires JSON content type; token is passed in body
    headers = {
        "Content-Type": "application/json"
    }

    try:
        print(f"Sending WhatsApp message via OnBBits API Campaign to: {request_payload.get('destination')}")
        response = requests.post(
            url=api_url,
            headers=headers,
            json=request_payload,
            timeout=30
        )

        # Check for HTTP errors (status codes 4xx or 5xx)
        response.raise_for_status()

        # Parse and return JSON response
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            response_data = {"status": "success", "raw_response": response.text}

        print("Message sent successfully!")
        print("Response:")
        print(json.dumps(response_data, indent=2))
        return response_data

    except requests.exceptions.HTTPError as http_err:
        print(f"[HTTP Error] Request failed with status code {response.status_code}: {http_err}")
        try:
            error_details = response.json()
            print("Server error details:")
            print(json.dumps(error_details, indent=2))
        except (json.JSONDecodeError, AttributeError):
            print(f"Server response: {response.text}")
        return None

    except requests.exceptions.ConnectionError as conn_err:
        print(f"[Network Error] Failed to connect to OnBBits API: {conn_err}")
        return None

    except requests.exceptions.Timeout as timeout_err:
        print(f"[Timeout Error] Request timed out: {timeout_err}")
        return None

    except requests.exceptions.RequestException as req_err:
        print(f"[Request Error] An unexpected error occurred: {req_err}")
        return None


if __name__ == "__main__":
    response = send_whatsapp_message(
        API_CAMPAIGN_URL,
        API_KEY,
        PAYLOAD
    )
