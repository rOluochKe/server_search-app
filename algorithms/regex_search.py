import re
# from .utils.read_file import read_file
# from .utils.measure_execution_time import measure_execution_time
# from .utils.print_search_result import print_search_result


def regex_search(file_path: list[str], query: str) -> tuple[bool, str]:
    """
    Search for a pattern in the file contents using regular expressions.

    Args:
    - file_path (list[str]): The list of strings representing the file content.
    - query (str): The regular expression pattern to search for in the file
                   content.

    Returns:
    - tuple[bool, str]: A tuple containing a boolean indicating whether the
                        pattern was found and the matched line with line
                        number if found, or None if not found.
    """
    if not isinstance(file_path, list):
        raise TypeError("File content must be provided as a list of strings.")

    # Check if query is empty
    if not query:
        return False, None

    pattern = re.compile(query)  # Compile the pattern for efficiency
    for line_number, line in enumerate(file_path, start=1):
        if pattern.search(line.strip()):
            # Match found, return the line with line number
            return True, f"Line {line_number}: {line.strip()}"
    return False, None  # No match found


# # Usage
# query = "3;0;1;28;0;7;5;0;"
# file_path = read_file('200k.txt')
# search_name = "regex"

# # Call regex_search with the actual file content
# execution_time, found, matched_line = measure_execution_time(
#     regex_search, file_path, query)

# # Print the search result and execution time
# print_search_result(found, matched_line, query, search_name, execution_time)
