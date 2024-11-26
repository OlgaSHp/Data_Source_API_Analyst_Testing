# **Data Cleaning Approach**

This document describes the techniques and processes used to clean and structure the data extracted from the GitHub API. The goal is to ensure the data is consistent, accurate, and ready for further analysis or integration.

---

## **1. Handling Duplicate Data**
- **Issue**: Duplicate entries may occur during pagination or when re-fetching data after rate limits.
- **Approach**:
  - Remove duplicate rows based on unique identifiers (e.g., repository `id` or commit `sha`).
  - Example using Python and pandas:
    ```python
    import pandas as pd

    # Assuming `data` is a list of dictionaries
    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset="id")  # Remove duplicates by 'id' column
    ```

---

## **2. Handling Missing or Invalid Data**
- **Issue**: Some fields may be missing or contain null/invalid values.
- **Approach**:
  - Identify critical fields and validate their completeness.
  - Replace missing values with defaults or remove rows/columns as needed.
  - Example:
    ```python
    # Remove rows with missing values
    df = df.dropna()

    # Replace missing values in specific columns
    df['field_name'] = df['field_name'].fillna('default_value')
    ```

---

## **3. Field Normalization**
- **Issue**: Data fields may have inconsistent formats (e.g., text casing, date formats).
- **Approach**:
  - Normalize string fields to lowercase for consistency.
  - Convert date fields to a standard datetime format.
  - Example:
    ```python
    df['field_name'] = df['field_name'].str.lower()  # Convert text to lowercase
    df['date_field'] = pd.to_datetime(df['date_field'])  # Convert to datetime
    ```

---

## **4. Flattening Nested JSON Structures**
- **Issue**: API responses often contain nested JSON structures that are difficult to analyze.
- **Approach**:
  - Flatten nested JSON fields into a tabular format using Python's pandas library.
  - Example:
    ```python
    from pandas import json_normalize

    # Assuming `response` is the JSON response from the API
    flat_data = json_normalize(response['items'])  # Flatten the 'items' field
    ```

---

## **5. Dealing with Large Datasets**
- **Issue**: Extracting large datasets may cause performance issues or rate-limit errors.
- **Approach**:
  - Use batch processing to handle large datasets incrementally.
  - Save intermediate results to avoid re-fetching data in case of interruptions.
  - Example:
    ```python
    # Save to a CSV file
    df.to_csv('output.csv', index=False)

    # Load the data later for further processing
    df = pd.read_csv('output.csv')
    ```

---

## **6. Data Validation**
- **Issue**: Extracted data may not meet expected standards or formats.
- **Approach**:
  - Perform validations on critical fields to ensure accuracy and completeness.
  - Example:
    ```python
    # Validate non-null critical fields
    assert df['field_name'].notnull().all(), "Critical field contains null values"

    # Validate data types
    assert df['numeric_field'].dtype == 'int64', "Field type mismatch"
    ```

---

## **7. Exporting Cleaned Data**
- **Formats**:
  - Export cleaned data in formats suitable for downstream processes:
    - `.csv` for tabular data.
    - `.json` for nested data.
- **Example**:
  ```python
  # Export to CSV
  df.to_csv('cleaned_data.csv', index=False)

  # Export to JSON
  df.to_json('cleaned_data.json', orient='records')
