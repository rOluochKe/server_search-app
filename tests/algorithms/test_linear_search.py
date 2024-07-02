from ...algorithms.linear_search import linear_search


def test_linear_search_pattern_not_found():
    """Test case when the pattern is not found"""
    query = "xyz"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = linear_search(file_path, query)
    assert found is False
    assert matched_line is None


def test_linear_search_empty_file_content():
    """Test case with empty file content"""
    query = "abc"
    file_path = []
    found, matched_line = linear_search(file_path, query)
    assert found is False
    assert matched_line is None
