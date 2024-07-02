import mmap
import os
from typing import List, Tuple
# from .utils.read_file import read_file
# from .utils.measure_execution_time import measure_execution_time
# from .utils.print_search_result import print_search_result


def mmap_search(file_path: List[str], query: str) -> Tuple[bool, str]:
    """
    Search for a pattern in file content using mmap.

    Args:
        file_path (List[str]): The list of strings representing the file content.
        query (str): The pattern to search for in the file content.

    Returns:
        Tuple[bool, str]: A tuple containing a boolean indicating whether the
            pattern was found and the matched line content (without line number)
            if found, or None if not found.
    """
    if not query:
        raise ValueError("Empty query string is not allowed.")

    if not isinstance(file_path, list):
        raise TypeError("File path must be a list of strings.")

    try:
        # Create a temporary file to hold the file content
        with open("temp_file.txt", "w") as temp_file:
            temp_file.writelines(file_path)

        # Open the temporary file in read-only mode
        with open("temp_file.txt", "r") as temp_file:
            # Map the file content into memory
            with mmap.mmap(temp_file.fileno(), 0, access=mmap.ACCESS_READ) as buf:
                # Iterate over each line in the file
                for ln_num, line in enumerate(iter(buf.readline, b""), start=1):
                    # Search for the exact match of the query in the line
                    if query.encode() in line:
                        # Return only the matched line content (without line number)
                        return True, line.decode().strip()
        return False, None

    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return False, None

    finally:
        # Remove the temporary file
        os.remove("temp_file.txt")


# # Usage
# query = "3;0;1;28;0;7;5;0;"
# file_path = read_file('200k.txt')
# search_name = "mmap"

# # Call mmap_search with the actual file content
# execution_time, found, matched_line = measure_execution_time(
#     mmap_search, file_path, query)

# # Print the search result and execution time
# print_search_result(found, matched_line, query, search_name, execution_time)
