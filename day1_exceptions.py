"""Day 1: Exceptions examples and utilities for learning

Contains small functions demonstrating:
- file reading with exception handling
- JSON decode error handling
- custom exception usage
- safe division wrapper that handles ZeroDivisionError

This file is intended to be used together with tests/test_day1_exceptions.py
"""

import json
from typing import Any


class InvalidUserData(Exception):
    """Custom exception raised when required user fields are missing."""
    pass


def read_json_file(path: str) -> Any:
    """Read and parse a JSON file.

    Raises:
        FileNotFoundError: if the file does not exist.
        ValueError: if the file is not valid JSON.
    Returns the parsed JSON object on success.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Let the caller handle missing files (often a test will assert this)
        raise
    except json.JSONDecodeError as e:
        # Normalize to ValueError for consumers
        raise ValueError("Invalid JSON file") from e


def validate_user(data: dict) -> bool:
    """Validate that a user dict contains required fields.

    Raises InvalidUserData when a required field is missing.
    Returns True when valid.
    """
    if not isinstance(data, dict):
        raise InvalidUserData("user data must be a dict")
    if "username" not in data:
        raise InvalidUserData("missing username")
    if "password" not in data:
        raise InvalidUserData("missing password")
    # simple rule: password length >= 3
    if len(data.get("password", "")) < 3:
        raise InvalidUserData("password too short")
    return True


def divide(a: float, b: float) -> float:
    """Direct division that may raise ZeroDivisionError."""
    return a / b


def safe_divide(a: float, b: float):
    """Wrapper that returns None when division by zero occurs."""
    try:
        return divide(a, b)
    except ZeroDivisionError:
        return None
