# utils/data_loader.py

import json
from pathlib import Path


def load_test_data(file_name, key=None):
    """
    Loads test data from any JSON file in the 'data' folder.

    Args:
        file_name (str): The name of the JSON file (e.g., 'customer_test_data.json')
        key (str, optional): If your JSON has multiple sections, specify the key to get only that data.

    Returns:
        list or dict: Returns the JSON content (or a specific key if provided)
    """
    # Get the project root folder
    current_dir = Path(__file__).resolve().parent
    data_file = current_dir.parent / "data" / file_name

    if not data_file.exists():
        raise FileNotFoundError(f"File not found: {data_file}")

    with open(data_file, "r") as f:
        data = json.load(f)

    # If a key is provided, return only that slice of the data
    if key:
        return data.get(key, [])

    return data


def get_test_case(file_name, key, index):
    """
    Fetch a specific test case from the JSON file using category and index.

    Args:
        file_name (str): The JSON file name (e.g., 'customer_test_data.json')
        key (str): Category in the JSON (e.g., 'valid_customers')
        index (int): Index of the test case in that category

    Returns:
        dict: The specific test case dictionary
    """
    cases = load_test_data(file_name, key)
    if not isinstance(cases, list):
        raise ValueError(f"The key '{key}' does not contain a list in {file_name}.")
    if index < 0 or index >= len(cases):
        raise IndexError(f"Index {index} out of range for key '{key}' in {file_name}.")
    return cases[index]