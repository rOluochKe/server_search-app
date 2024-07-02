import pytest
from ....algorithms.utils.read_file import read_file


def test_read_file_success(tmp_path):
    """
    Tests successful reading of a valid text file.
    """
    file_content = ["Line 1\n", "Line 2\n", "Line 3"]
    test_file = tmp_path / "test.txt"
    test_file.write_text("".join(file_content))

    lines = read_file(str(test_file))
    assert lines == file_content


def test_read_file_non_string_filename():
    """
    Tests raising ValueError for non-string filename.
    """
    with pytest.raises(ValueError):
        read_file(123)  # Pass a non-string argument


def test_read_file_missing_file(tmp_path):
    """
    Tests handling of a missing file (FileNotFoundError).
    """
    missing_file = tmp_path / "missing.txt"

    lines = read_file(str(missing_file))
    assert lines is None  # Verify None is returned


def test_read_file_empty_file(tmp_path):
    """
    Tests reading an empty file.
    """
    empty_file = tmp_path / "empty.txt"
    empty_file.touch()

    lines = read_file(str(empty_file))
    assert lines == []  # Verify an empty list is returned
