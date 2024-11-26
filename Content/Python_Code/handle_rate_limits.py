import time
import requests
from auth import HEADERS, BASE_URL


class GitHubRateLimiter:
    """A class to handle GitHub API rate limiting."""

    def __init__(self, base_url, headers):
        """
        Initialize the GitHubRateLimiter class.
        :param base_url: The base URL for the GitHub API
        :param headers: Headers for API authentication
        """
        self.base_url = base_url
        self.headers = headers

    def check_rate_limit(self):
        """
        Check the current rate limit for the GitHub API.
        :return: Dictionary with rate limit details
        """
        url = f"{self.base_url}/rate_limit"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            rate_limit = response.json().get("rate", {})
            print("Rate Limit:", rate_limit)
            return rate_limit
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
            return None

    def wait_if_rate_limited(self):
        """
        Pause execution if the rate limit is exceeded.
        """
        rate_limit = self.check_rate_limit()
        if rate_limit and rate_limit.get("remaining", 0) == 0:
            reset_time = rate_limit.get("reset", 0)
            wait_time = reset_time - int(time.time())
            if wait_time > 0:
                print(f"Rate limit exceeded. Waiting {wait_time} seconds.")
                time.sleep(wait_time)
            else:
                print("Rate limit reset time has already passed. Continuing...")


if __name__ == "__main__":
    # Initialize the GitHubRateLimiter class
    rate_limiter = GitHubRateLimiter(BASE_URL, HEADERS)

    # Example: Check the current rate limit
    print("Checking rate limit:")
    rate_limiter.check_rate_limit()

    # Example: Wait if rate limit is exceeded
    print("\nTesting rate limit handling:")
    rate_limiter.wait_if_rate_limited()
