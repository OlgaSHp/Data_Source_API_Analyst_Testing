# GitHub API Documentation

This file provides detailed notes on the GitHub API endpoints used in this assignment, their usage, and examples.

---

## 1. Search Repositories

- **Endpoint**: `/search/repositories`
- **Method**: `GET`
- **Description**: Retrieves a list of repositories based on search criteria.
- **URL Format**:
```plaintext
https://api.github.com/search/repositories?q={query}&sort={sort}&order={order}
```
- **Parameters**:
- `q` (required): The search keywords or qualifiers (e.g., `language:Python`).
- `sort` (optional): The sort field (e.g., `stars`, `forks`, or `updated`).
- `order` (optional): The sort order (`asc` or `desc`).
- **Headers**:
- `Authorization`: `Bearer {token}` (for authentication).
- `X-GitHub-Api-Version`: `2022-11-28` (GitHub API version header).
- **Example**:
```plaintext
GET https://api.github.com/search/repositories?q=language:Python&sort=stars&order=desc
```
- **Example Response**:
```json
{
  "total_count": 1234567,
  "items": [
    {
      "id": 123456,
      "name": "example-repo",
      "full_name": "user/example-repo",
      "stargazers_count": 10000
    }
  ]
}
```
---

## 2. List Commits

- **Endpoint**: `/repos/{owner}/{repo}/commits`
- **Method**: `GET`
- **Description**: Retrieves the list of commits for a specific repository.
- **URL Format**:
```plaintext
https://api.github.com/repos/{owner}/{repo}/commits
```
- **Parameters**:
- `{owner}`: The owner of the repository.
- `{repo}`: The name of the repository.
- **Optional filters**:
  - `author`: Filter commits by author.
  - `since`: ISO 8601 timestamp to fetch commits after a specific date.
  - `until`: ISO 8601 timestamp to fetch commits before a specific date.
- **Headers**:
- `Authorization`: `Bearer {token}`
- `X-GitHub-Api-Version`: `2022-11-28`
- **Example**:
```plaintext
GET https://api.github.com/repos/torvalds/linux/commits
```
- **Example Response**:
```json

[
  {
    "sha": "abc123",
    "commit": {
      "message": "Initial commit",
      "author": { "name": "Linus Torvalds" }
    }
  }
]
```
## 3. Get Repository Contents

- **Endpoint**: /repos/{owner}/{repo}/contents/{path}
- **Method**: GET
- **Description**: Retrieves the contents of a file or directory in a repository.
- **URL Format**:
```plaintext
https://api.github.com/repos/{owner}/{repo}/contents/{path}
```
- **Parameters**:
- `{owner}`: The owner of the repository.
- `{repo}`: The name of the repository.
- `{path}`: The file or directory path.
- **Headers**:
- `Authorization`: `Bearer {token}`
- `X-GitHub-Api-Version`: `2022-11-28`
- **Example**:
```plaintext
GET https://api.github.com/repos/torvalds/linux/contents/README.md
```
- **Example Response:**
```json
{
  "name": "README.md",
  "path": "README.md",
  "content": "SGVsbG8gd29ybGQ="
}
```
---

## 4. Validate Token

- **Endpoint**: `/user`
- **Method**: `GET`
- **Description**: Confirms that the provided Personal Access Token (PAT) is valid.
- **URL**:
```plaintext
https://api.github.com/user
```
- **Headers**:
- `Authorization`: `Bearer {token}`
- `X-GitHub-Api-Version`: `2022-11-28`
- **Example**:
```plaintext
GET https://api.github.com/user
```
- **Example Response:**
```json
{
  "login": "example_username",
  "id": 123456,
  "type": "User",
  "site_admin": false
}
```
5. Check Rate Limits

- **Endpoint**: `/user`
- **Method**: `GET`
- **Description**: Monitors the remaining API requests and reset time for the current rate limit window.
URL:
```plaintext
https://api.github.com/rate_limit
```
- **Headers**:
- `Authorization`: `Bearer {token}`
- `X-GitHub-Api-Version`: `2022-11-28`
- **Example**:
```plaintext
GET https://api.github.com/rate_limit
```
- **Example Response:**
```json
{
  "rate": {
    "limit": 5000,
    "remaining": 4999,
    "reset": 1638555200
  }
}
```
---

## **Rate Limit and Pagination Notes**

### **Rate Limits**
- Authenticated requests are limited to **5,000 requests per hour**.
- Use the `/rate_limit` endpoint to monitor the current rate limit status, including:
  - **Total limit**: The maximum number of requests allowed.
  - **Remaining requests**: The number of requests you can still make in the current time window.
  - **Reset time**: The time when the rate limit will reset (in UNIX timestamp format).

### **Pagination**
- Many GitHub API endpoints return paginated results to manage large datasets. 
- To handle pagination, include the following query parameters in your request:
  - `per_page`: Specifies the number of results to return per page (maximum: 100).
  - `page`: Specifies the page number to fetch.

### **Example: Paginated Request**
Fetch repositories with a maximum of 100 results per page, and retrieve the second page:

- **Example**:
```plaintext
GET https://api.github.com/search/repositories?q=language:Python&per_page=100&page=2
```