def print_search_result(found: bool, matched_line:
                        str, query: str, search_name:
                        str, execution_time: float) -> None:
    """
    Print the search result and execution time.

    Args:
    - found (bool): Indicates whether the query was found.
    - matched_line (str or None): The matched line if found, None otherwise.
    - query (str): The query string that was searched for.
    - search_name (str): The name of the search function used.
    - execution_time (float): The execution time of the search function in
                              seconds.
    """
    if found:
        print(f"String '{matched_line}' found in the file.")
    else:
        print(f"String '{query}' not found in the file.")

    print(f"{search_name} search execution time: {execution_time} seconds")
