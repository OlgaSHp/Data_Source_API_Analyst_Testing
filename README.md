# **Data-Source-API-Analyst-Test**

This repository is created for the Data Source API Analyst role assignment. It includes testing GitHub API endpoints, creating API requests in Postman or Google Colab, and handling pagination, rate limits, and errors.

---

## **Repository Structure**
- **Content/**
  - Contains API documentation, Python code for authentication, data extraction, error handling, and pagination.
  - **Files included**:
    - `API_Documentation.txt`: Notes on GitHub API endpoints used in this assignment.
    - `Python_Code/`: Python scripts for key functionalities:
      - `auth.py`: Handles token-based authentication.
      - `extract_data.py`: Extracts data from API endpoints.
      - `handle_rate_limits.py`: Manages rate limits during API requests.
      - `pagination.py`: Handles data pagination for large datasets.
    - `Troubleshooting_Guide.txt`: Common issues and solutions encountered during testing.
    - `Data_Cleaning_Approach.txt`: Techniques for cleaning and organizing the extracted data.
  
- **Postman_Collection/**
  - Includes the Postman collection file or Google Colab notebook used for API testing.
  - **Files included**:
    - `Github_API_Test.postman_collection.json`: Postman collection of tested GitHub API endpoints.
    - `Github_API_Test.ipynb`: Colab notebook (alternative to Postman), demonstrating API requests.

- **README.md**
  - Explains the purpose of the repository and details the approach to solving the assignment.

---

## **Endpoints Tested**
The following GitHub API endpoints were tested:

1. **Search Repositories**:
   - **Endpoint**: `/search/repositories`
   - **Purpose**: Retrieves repositories matching specific search criteria.
   
2. **List Commits**:
   - **Endpoint**: `/repos/{owner}/{repo}/commits`
   - **Purpose**: Fetches commit history for a specific repository.
   
3. **Get Contents**:
   - **Endpoint**: `/repos/{owner}/{repo}/contents/{path}`
   - **Purpose**: Retrieves the contents of files within a repository.

4. **User-Related Endpoints**:
   - **Validate Token**:
     - **Endpoint**: `/user`
     - **Purpose**: Confirms the validity of the Personal Access Token (PAT) and retrieves user details.
     - **Example Request**:
       ```plaintext
       GET https://api.github.com/user
       ```
     - **Example Response**:
       ```json
       {
         "login": "example_username",
         "id": 123456,
         "type": "User",
         "site_admin": false
       }
       ```
   - **Check Rate Limits**:
     - **Endpoint**: `/rate_limit`
     - **Purpose**: Monitors API usage and remaining requests for the current rate limit window.
     - **Example Request**:
       ```plaintext
       GET https://api.github.com/rate_limit
       ```
     - **Example Response**:
       ```json
       {
         "rate": {
           "limit": 5000,
           "remaining": 4999,
           "reset": 1638555200
         }
       }
       ```

   - **List User Repositories**:
     - **Endpoint**: `/user/repos`
     - **Purpose**: Retrieves repositories accessible by the authenticated user.
     - **Example Request**:
       ```plaintext
       GET https://api.github.com/user/repos
       ```
     - **Example Response**:
       ```json
       [
         {
           "id": 123456,
           "name": "example-repo",
           "full_name": "username/example-repo",
           "private": false
         }
       ]
       ```

---

## **Steps to Run**

1. **Set Up GitHub API Credentials**:
   - Generate a **Personal Access Token (PAT)** from your GitHub account:
     - Navigate to **Settings > Developer Settings > Personal Access Tokens > Tokens (classic)**.
     - Generate a token with the required scopes (e.g., `repo` for repository access).
   - Configure the token:
     - In **Postman**: Add the token as an environment variable.
     - In **Google Colab**: Replace the placeholder in the `TOKEN` variable with your PAT.

2. **Use Postman or Google Colab to Test Endpoints**:
   - **Postman**:
     - Import the `Github_API_Test.postman_collection.json` file.
     - Set up the `{{token}}` environment variable.
     - Send requests to validate responses.
   - **Google Colab**:
     - Open the `Github_API_Test.ipynb` notebook.
     - Update the `TOKEN` variable with your PAT.
     - Execute the cells to test API endpoints.

3. **Follow the Troubleshooting Guide for Common Issues**:
   - Check `Troubleshooting_Guide.txt` for solutions to errors like:
     - `401 Unauthorized`: Ensure your token is valid and correctly set.
     - `403 Forbidden`: Monitor API rate limits and retry after the reset period.
     - Pagination: Handle large datasets by iterating over pages.

---

## **Key Features**
- **Authentication**: Token-based authentication to securely access GitHub API endpoints.
- **Pagination Handling**: Fetch data in batches when dealing with large datasets.
- **Rate Limit Management**: Monitor and handle rate limits to avoid disruptions.
- **Error Handling**: Detect and manage errors like invalid tokens or exceeded rate limits.

