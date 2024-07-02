from typing import List, Tuple, Optional
# from .utils.read_file import read_file
# from .utils.measure_execution_time import measure_execution_time
# from .utils.print_search_result import print_search_result


def linear_search(file_path: List[str], query: str) -> Tuple[bool, Optional[str]]:
    """
    Search for a pattern in file content using linear search.

    Args:
    - file_path (List[str]): The list of strings representing the file content.
    - query (str): The pattern to search for in the file content.

    Returns:
    - Tuple[bool, Optional[str]]: A tuple containing a boolean indicating whether the
                                  pattern was found and the matched line with line
                                  number if found, or None if not found.
    """
    try:
        for ln_num, line in enumerate(file_path, start=1):
            if query.strip() == line.strip():
                # Return True and the matched line with line number
                return True, f"Line {ln_num}: {line.strip()}"
        return False, None  # No match found
    except Exception as e:
        raise e


# # Usage
# query = "3;0;1;28;0;7;5;0;"
# file_path = read_file('200k.txt')
# search_name = "linear"

# # Call linear_search with the actual file content
# execution_time, found, matched_line = measure_execution_time(
#     linear_search, file_path, query)

# # Print the search result and execution time
# print_search_result(found, matched_line, query, search_name, execution_time)
