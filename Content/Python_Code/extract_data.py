import requests
from auth import HEADERS, BASE_URL


class GitHubAPI:
    """A class to interact with the GitHub API."""

    def __init__(self, base_url, headers):
        """
        Initialize the GitHubAPI class with a base URL and headers.
        :param base_url: The base URL for the GitHub API
        :param headers: Headers for API authentication
        """
        self.base_url = base_url
        self.headers = headers

    def search_repositories(self, query="language:Python", sort="stars", order="desc"):
        """
        Search for repositories based on a query.
        :param query: Search query (e.g., language:Python)
        :param sort: Sort parameter (e.g., stars, forks)
        :param order: Order parameter (e.g., asc, desc)
        :return: List of repository items
        """
        url = f"{self.base_url}/search/repositories"
        params = {"q": query, "sort": sort, "order": order}
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json().get("items", [])
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def list_commits(self, owner, repo):
        """
        List commits for a specific repository.
        :param owner: Repository owner
        :param repo: Repository name
        :return: List of commits
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def get_contents(self, owner, repo, path):
        """
        Retrieve contents of a file or directory.
        :param owner: Repository owner
        :param repo: Repository name
        :param path: Path to the file or directory
        :return: JSON response with contents
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/contents/{path}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")


if __name__ == "__main__":
    # Initialize the GitHubAPI class
    github_api = GitHubAPI(BASE_URL, HEADERS)

    # Example 1: Search for Python repositories sorted by stars
    print("Searching for Python repositories sorted by stars:")
    repositories = github_api.search_repositories()
    if repositories:
        for repo in repositories[:5]:  # Show only the top 5 results
            print(f"Repository: {repo['full_name']} | Stars: {repo['stargazers_count']}")

    # Example 2: List commits for a specific repository
    print("\nListing commits for the 'microsoft/vscode' repository:")
    commits = github_api.list_commits("microsoft", "vscode")
    if commits:
        for commit in commits[:5]:  # Show only the top 5 commits
            print(f"Commit: {commit['commit']['message']} | Author: {commit['commit']['author']['name']}")

    # Example 3: Get contents of a specific path
    print("\nRetrieving contents of the README file in 'microsoft/vscode':")
    contents = github_api.get_contents("microsoft", "vscode", "README.md")
    if contents:
        print(contents)
