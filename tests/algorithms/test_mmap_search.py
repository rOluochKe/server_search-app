import pytest
from ...algorithms.mmap_search import mmap_search


def test_mmap_search_pattern_not_found():
    """Tests if the function returns False for a non-existent pattern."""
    query = "xyz"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = mmap_search(file_path, query)
    assert found is False
    assert matched_line is None


def test_mmap_search_empty_file_content():
    """Tests if the function handles an empty file."""
    query = "any_pattern"
    file_path = []
    found, matched_line = mmap_search(file_path, query)
    assert found is False
    assert matched_line is None


def test_mmap_search_empty_query():
    """Tests if the function handles an empty query string."""
    query = ""
    file_path = ["Line 1: This is a test line."]
    with pytest.raises(ValueError):
        mmap_search(file_path, query)


def test_mmap_search_invalid_file_type():
    """Tests if the function handles a non-list input for file content."""
    query = "test_pattern"
    file_content = "This is not a list."
    with pytest.raises(TypeError):
        mmap_search(file_content, query)
