import pytest
from ....algorithms.utils.print_search_result import print_search_result


@pytest.fixture
def expected_output(request):
    return request.param


@pytest.mark.parametrize(
    "found, matched_line, query, search_name, execution_time, expected_output", [
        # Test case when query is found in the file
        (
            True,
            "This is the line where the query was found.",
            "query",
            "linear",
            0.002,
            "String 'This is the line where the query was found.' found in the file.\nlinear search execution time: 0.002 seconds"
        ),
        # Test case when query is not found in the file
        (
            False,
            None,
            "query",
            "linear",
            0.002,
            "String 'query' not found in the file.\nlinear search execution time: 0.002 seconds"
        ),
        # Test case when matched line is None
        (
            True,
            None,
            "query",
            "linear",
            0.002,
            "String 'None' found in the file.\nlinear search execution time: 0.002 seconds"
        ),
        # Test case when execution time is zero
        (
            True,
            "This is the line where the query was found.",
            "query",
            "linear",
            0,
            "String 'This is the line where the query was found.' found in the file.\nlinear search execution time: 0 seconds"
        ),
        # Test case when matched line is empty
        (
            True,
            "",
            "query",
            "linear",
            0.002,
            "String '' found in the file.\nlinear search execution time: 0.002 seconds"
        ),
        # Test case when execution time is a large float
        (
            True,
            "This is the line where the query was found.",
            "query",
            "linear",
            999999.999999999,
            "String 'This is the line where the query was found.' found in the file.\nlinear search execution time: 999999.999999999 seconds"
        ),
        # Test case when execution time is negative
        (
            True,
            "This is the line where the query was found.",
            "query",
            "linear",
            -0.002,
            "String 'This is the line where the query was found.' found in the file.\nlinear search execution time: -0.002 seconds"
        ),
        # Test case when search name is an empty string
        (
            True,
            "This is the line where the query was found.",
            "query",
            "",
            0.002,
            "String 'This is the line where the query was found.' found in the file.\n search execution time: 0.002 seconds"
        ),
    ], indirect=['expected_output'])
def test_print_search_result(capsys, found, matched_line, query, search_name,
                             execution_time, expected_output):
    print_search_result(found, matched_line, query,
                        search_name, execution_time)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
