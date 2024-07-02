# from .utils.print_search_result import print_search_result
# from .utils.read_file import read_file
import time


def merge(left: list[str], right: list[str]) -> list[str]:
    """
    Merge two sorted lists into a single sorted list.

    Args:
    - left (list[str]): The left sorted list.
    - right (list[str]): The right sorted list.

    Returns:
    - list[str]: A merged sorted list.
    """
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i].strip() < right[j].strip():
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged


def merge_sort(data: list[str]) -> list[str]:
    """
    Sort a list using the Merge Sort algorithm.

    Args:
    - data (list[str]): The list to be sorted.

    Returns:
    - list[str]: A sorted list.
    """
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def binary_search(data: list[str], query: str, low: int, high:
                  int) -> tuple[bool, str]:
    """
    Search for a string in a sorted list using Binary Search.

    Args:
    - data (list[str]): The sorted list to search in.
    - query (str): The string to search for.
    - low (int): The lower bound index for the search.
    - high (int): The upper bound index for the search.

    Returns:
    - tuple[bool, str or None]: A tuple indicating whether the query was found
                                and the matched line if found.
    """
    if low > high:
        return False, None  # String not found

    mid = (low + high) // 2
    if data[mid].strip() == query.strip():
        return True, data[mid].strip()  # String found and return the line
    elif data[mid].strip() < query.strip():
        return binary_search(data, query, mid + 1, high)
    else:
        return binary_search(data, query, low, mid - 1)


def measure_execution_time(search_func: callable, file_path: list[str],
                           query: str) -> tuple[float, bool, str]:
    """
    Measure the execution time of a search function.

    Args:
    - search_func (callable): The search function to be executed.
    - file_path (list[str]): The path to the file to be searched.
    - query (str): The query string to search for.

    Returns:
    - tuple[float, bool, str or None]: A tuple containing the execution time
                                       (in seconds), a boolean indicating
                                       whether the query was found, and the
                                       matched line if found.
    """
    start_time = time.time()
    found, matched_line = search_func(file_path, query, 0, len(file_path) - 1)
    end_time = time.time()
    return end_time - start_time, found, matched_line


# # Usage
# query = "3;0;1;28;0;7;5;0;"
# file_path = read_file('200k.txt')
# search_name = "binary"

# # Sort the data
# data = merge_sort(file_path)

# # Call binary_search with the actual file content
# execution_time, found, matched_line = measure_execution_time(
#     binary_search, data, query)

# # Print the search result and execution time
# print_search_result(found, matched_line, query, search_name, execution_time)
