import pytest

from ...algorithms.regex_search import regex_search


def test_regex_search_found():
    """Tests if the function finds a matching line."""
    file_content = ["This line has no match",
                    "This line;3;1;8;0;7;5;0; matches"]
    query = "3;1;8;0;7;5;0;"
    found, matched_line = regex_search(file_content, query)
    assert found is True
    assert matched_line == "Line 2: This line;3;1;8;0;7;5;0; matches"


def test_regex_search_not_found():
    """Tests if the function returns None for no match."""
    file_content = ["Line 1", "Line 2", "Line 3"]
    query = "This is not a pattern"
    found, matched_line = regex_search(file_content, query)
    assert found is False
    assert matched_line is None


def test_regex_search_empty_file():
    """Tests if the function handles empty file content."""
    file_content = []
    query = "test"
    found, matched_line = regex_search(file_content, query)
    assert found is False
    assert matched_line is None


def test_regex_search_invalid_file_type():
    """Tests if the function raises an error for non-list input."""
    with pytest.raises(TypeError):
        regex_search("invalid_file_type.txt", "query")


def test_regex_search_empty_query():
    """Tests if the function handles an empty query string."""
    file_content = ["Line 1", "Line 2"]
    query = ""
    found, matched_line = regex_search(file_content, query)
    assert found is False
    assert matched_line is None


def test_regex_search_case_insensitivity():
    """Tests if the function ignores case sensitivity."""
    file_content = ["This Line has a MATCH"]
    query = "(?i)match"
    found, matched_line = regex_search(file_content, query)
    assert found is True
    assert matched_line == "Line 1: This Line has a MATCH"


def test_regex_search_special_characters():
    """Tests if the function correctly handles special characters."""
    file_content = ["Line 1: $100 for you", "Line 2: Not $100 for me"]
    query = r"\$100"
    found, matched_line = regex_search(file_content, query)
    assert found is True
    assert matched_line.startswith("Line 1:")
    assert "100 for you" in matched_line


def test_regex_search_case_sensitivity():
    """Tests if the function is case-sensitive by default."""
    file_content = ["This line matches", "this Line does not match"]
    query = "matches"
    found, matched_line = regex_search(file_content, query)
    assert found is True
    assert matched_line == "Line 1: This line matches"


def test_regex_search_with_quantifiers():
    """Tests if the function correctly handles regex patterns with quantifiers."""
    file_content = ["Line 1: apple", "Line 2: aapple", "Line 3: aaapple"]
    query = r"a{2,}ple"  # Matches "aaapple"
    found, matched_line = regex_search(file_content, query)
    assert found is False  # Corrected assertion
