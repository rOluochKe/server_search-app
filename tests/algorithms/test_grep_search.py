import pytest
from ...algorithms.grep_search import grep_search
import subprocess


@pytest.fixture
def mock_read_file(monkeypatch):
    def mock_read_file_func(file_path):
        return ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    monkeypatch.setattr("my_module.read_file", mock_read_file_func)


def test_grep_search_pattern_found():
    query = "def"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = grep_search(file_path, query)
    assert found is True
    assert matched_line == "Line 2: def"


def test_grep_search_pattern_not_found():
    query = "xyz"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = grep_search(file_path, query)
    assert found is False
    assert matched_line is None


def test_grep_search_command_failure(mocker):
    # Mock subprocess.run to simulate an error
    query = "abc"
    mocker.patch("subprocess.run",
                 side_effect=subprocess.CalledProcessError(returncode=1, cmd="grep"))
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = grep_search(file_path, query)
    assert found is False
    assert matched_line is None


def test_grep_search_special_characters_in_pattern():
    query = "3;0;1;28;0;7;5;0;"
    file_path = ["Line 1: data", "Line 2: another pattern"]
    found, matched_line = grep_search(file_path, query)
    assert found is False
    assert matched_line is None  # Escaping should handle special characters


def test_grep_search_empty_file_content():
    query = "abc"
    file_path = []
    found, matched_line = grep_search(file_path, query)
    assert found is False
    assert matched_line is None


def test_grep_search_multiple_matches():
    query = "Line"
    file_path = ["Line 1: abc", "Line 2: def", "Line 3: ghi"]
    found, matched_line = grep_search(file_path, query)
    assert found is True
    assert matched_line == "Line 1: abc"  # First match is returned
