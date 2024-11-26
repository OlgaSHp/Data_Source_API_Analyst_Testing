import requests
from auth import HEADERS, BASE_URL


class PageFetcher:
    def __init__(self, base_url, headers):
        """
        Initializes the PageFetcher with a base URL and headers.

        :param base_url: Base URL for the API
        :param headers: Headers to include in API requests
        """
        self.base_url = base_url
        self.headers = headers

    def fetch_paginated_results(self, url, max_pages=None):
        """
        Fetches a limited number of paginated results from the given API endpoint.

        :param url: API endpoint with pagination
        :param max_pages: Maximum number of pages to fetch (optional, for testing purposes)
        :return: List of all results from the fetched pages
        """
        results = []
        page_count = 0  # To track the number of pages fetched

        while url:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

            data = response.json()
            results.extend(data)

            # Increment the page count
            page_count += 1
            if max_pages and page_count >= max_pages:
                print(f"Stopping after fetching {page_count} pages (testing limit reached).")
                break

            # Check for the 'Link' header to find the next page URL
            link_header = response.headers.get('Link')
            if link_header:
                next_url = None
                for link in link_header.split(','):
                    if 'rel="next"' in link:
                        next_url = link.split(';')[0].strip('<> ')
                url = next_url
            else:
                url = None  # No more pages to fetch

        return results


if __name__ == "__main__":
    # Create an instance of the PageFetcher
    fetcher = PageFetcher(BASE_URL, HEADERS)

    # Initial URL for the first page
    initial_url = f"{BASE_URL}/repos/microsoft/vscode/contributors?per_page=10"

    try:
        # Set a maximum number of pages to fetch for testing (e.g., 2 pages)
        max_pages_to_fetch = 2
        contributors = fetcher.fetch_paginated_results(initial_url, max_pages=max_pages_to_fetch)
        print(f"Total contributors fetched: {len(contributors)}")
        for contributor in contributors:
            print(contributor)
    except Exception as e:
        print(f"Error fetching contributors: {e}")
