from ...algorithms.binary_search import binary_search


def test_binary_search_pattern_found_beginning():
    """Test case when the pattern is found at the beginning of the list"""
    query = "Line 1: abc"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = binary_search(
        file_path, query, 0, len(file_path) - 1)
    assert found is True
    assert matched_line == query


def test_binary_search_pattern_found_middle():
    """Test case when the pattern is found in the middle of the list"""
    query = "Line 2: def"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = binary_search(
        file_path, query, 0, len(file_path) - 1)
    assert found is True
    assert matched_line == query


def test_binary_search_pattern_found_end():
    """Test case when the pattern is found at the end of the list"""
    query = "Line 3: ghi"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = binary_search(
        file_path, query, 0, len(file_path) - 1)
    assert found is True
    assert matched_line == query


def test_binary_search_pattern_not_found():
    """Test case when the pattern is not found"""
    query = "xyz"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = binary_search(
        file_path, query, 0, len(file_path) - 1)
    assert found is False
    assert matched_line is None


def test_binary_search_empty_list():
    """Test case with empty list"""
    query = "abc"
    file_path = []
    found, matched_line = binary_search(
        file_path, query, 0, len(file_path) - 1)
    assert found is False
    assert matched_line is None


def test_binary_search_single_element():
    """Test case with single element in the list"""
    query = "Line 1: abc"
    file_path = ["Line 1: abc"]
    found, matched_line = binary_search(
        file_path, query, 0, len(file_path) - 1)
    assert found is True
    assert matched_line == query


def test_binary_search_duplicate_elements():
    """Test case with duplicate elements in the list"""
    query = "Line 1: abc"
    file_path = ["Line 1: abc", "Line 1: abc", "Line 1: abc"]
    found, matched_line = binary_search(
        file_path, query, 0, len(file_path) - 1)
    assert found is True
    assert matched_line == query
