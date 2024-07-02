import time
import pytest
from ....algorithms.utils.measure_execution_time import measure_execution_time


def mock_search_func(file_path, query):
    # Simulate different outcomes based on query
    if query == "found_query":
        return True, "This is the matched line"
    elif query == "large_file_query":
        return False, None
    elif query == "" or query is None:
        return False, None  # Not found for empty or null queries
    else:
        # Default for not found queries
        return False, "Line not found"


def test_measure_execution_time_success():
    """Tests if execution time is measured and query is found."""
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "test_file.txt", "found_query")
    assert execution_time > 0
    assert found is True
    assert matched_line == "This is the matched line"


def test_measure_execution_time_not_found():
    """Tests if execution time is measured and query is not found."""
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "test_file.txt", "not_found_query")
    assert execution_time > 0
    assert found is False
    assert matched_line == "Line not found"


def test_measure_execution_time_invalid_search_func():
    """Tests if function raises error for non-callable search_func."""
    with pytest.raises(TypeError):
        measure_execution_time("not_a_function", "test_file.txt", "query")


def test_measure_execution_time_large_file():
    """Tests if execution time is measured and file is very large."""
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "large_file.txt", "large_file_query")
    assert execution_time > 0
    assert found is False
    assert matched_line is None


def test_measure_execution_time_empty_query():
    """Tests if execution time is measured and query is empty."""
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "test_file.txt", "")
    assert execution_time > 0
    assert found is False
    assert matched_line is None


def test_measure_execution_time_null_query():
    """Tests if execution time is measured and query is None."""
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "test_file.txt", None)
    assert execution_time > 0
    assert found is False
    assert matched_line is None


def test_measure_execution_time_search_func_exception():
    """Tests if function handles exceptions raised by search_func."""
    def error_search_func(file_path, query):
        raise Exception("Search function error")
    with pytest.raises(Exception):
        measure_execution_time(error_search_func, "test_file.txt", "query")


def test_measure_execution_time_large_execution_time():
    """Tests if execution time is measured accurately for long-running search functions."""
    def mock_search_func_long_execution_time(file_path, query):
        time.sleep(2)  # Simulate long execution time
        return False, None
    execution_time, _, _ = measure_execution_time(
        mock_search_func_long_execution_time, "test_file.txt", "query")
    assert execution_time >= 2


def test_measure_execution_time_unicode_characters():
    """Tests if function handles Unicode characters in file content and query."""
    with open("unicode_file.txt", "w", encoding="utf-8") as file:
        file.write("日本語のテスト\nSpecial character: é")
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "unicode_file.txt", "한국어")
    assert execution_time > 0
    assert found is False
    assert matched_line == "Line not found"


def test_measure_execution_time_large_query():
    """Tests performance with a large query string."""
    large_query = "a" * 10000  # Create a large query string
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "test_file.txt", large_query)
    assert execution_time > 0
    assert found is False
    assert matched_line == "Line not found"


def test_measure_execution_time_large_file_performance():
    """Tests performance with a very large file."""
    with open("very_large_file.txt", "wb") as file:
        file.write(b"a" * 100000000)  # 100 MB of 'a's
    execution_time, found, matched_line = measure_execution_time(
        mock_search_func, "very_large_file.txt", "query")
    assert execution_time > 0
    assert found is False
    assert matched_line == "Line not found"
