import time


def measure_execution_time(search_func: callable, file_path: str,
                           query: str) -> tuple[float, bool, str]:
    """
    Measure the execution time of a search function.

    Args:
      - search_func (callable): The search function to be executed.
      - file_path (str): The path to the file to be searched.
      - query (str): The query string to search for.

    Returns:
      - tuple[float, bool, str]: A tuple containing the execution time
                                  (in seconds), a boolean indicating whether
                                  the query was found, and the matched line
                                  if found.
    """
    start_time = time.time()

    try:
        # Attempt to execute the search function
        found, matched_line = search_func(file_path, query)
    except PermissionError as e:
        # If file access is denied, raise a PermissionError
        raise PermissionError(
            f"Permission error accessing file: {file_path} - {e}")

    end_time = time.time()
    return end_time - start_time, found, matched_line
