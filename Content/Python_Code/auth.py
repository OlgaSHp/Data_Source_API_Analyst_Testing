import requests


BASE_URL = "https://api.github.com"
TOKEN = "your_personal_token"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

def test_auth():
    """Test if the authentication token is valid."""
    url = f"{BASE_URL}/user"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        print("Authentication successful:", response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        print(f"Other error occurred: {err}")
        raise


if __name__ == "__main__":
    # Test authentication
    try:
        test_auth()
    except Exception as e:
        print("Authentication failed. Exiting.")
        exit(1)
