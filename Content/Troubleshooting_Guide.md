# **Troubleshooting Guide**

This document addresses common issues encountered while working with the GitHub API and their resolutions.

---

## **Contents**
1. [Authentication Issues](#authentication-issues)
2. [Rate Limit Exceeded](#rate-limit-exceeded)
3. [Pagination Issues](#pagination-issues)
4. [Malformed Requests](#malformed-requests)
5. [Secondary Rate Limits](#secondary-rate-limits)

---

## **1. Authentication Issues**
- **Error**: `401 Unauthorized`
  - **Cause**: Invalid or expired Personal Access Token (PAT).
  - **Resolution**:
    1. Verify that the token is correct.
    2. Ensure the token has the necessary scopes (e.g., `repo` for repository access).
    3. Replace the token in your environment or code and re-test.

---

## **2. Rate Limit Exceeded**
- **Error**: `403 Forbidden`
  - **Cause**: Exceeded the main or secondary rate limits.
  - **Resolution**:
    1. Check the `/rate_limit` endpoint to monitor remaining requests.
    2. If `remaining` is `0`, wait until the `reset` time.
    3. For secondary rate limits:
        - Add delays between requests (e.g., `time.sleep(2)`).
        - Avoid making too many simultaneous requests to the same endpoint.

---

## **3. Pagination Issues**
- **Error**: Incomplete data retrieval.
  - **Cause**: Pagination was not handled properly.
  - **Resolution**:
    1. Ensure the `Link` header is used to identify the next page.
    2. Use a loop to fetch all pages until there is no `next` link.
    3. Check for `per_page` and `page` parameters in the query.

---

## **4. Malformed Requests**
- **Error**: `422 Unprocessable Entity`
  - **Cause**: Invalid parameters in the request.
  - **Resolution**:
    1. Double-check the parameters passed in the API request.
    2. Refer to the [GitHub API Documentation](https://docs.github.com/en/rest) for required fields.

---

## **5. Secondary Rate Limits**
- **Error**: `You have exceeded a secondary rate limit.`
  - **Cause**: Too many requests in a short time to a specific endpoint.
  - **Resolution**:
    1. Add a delay (e.g., `time.sleep(1-2 seconds)`) between requests.
    2. Avoid repetitive calls to endpoints by caching data locally when possible.
