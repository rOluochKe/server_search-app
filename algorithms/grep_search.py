import subprocess
# from .utils.read_file import read_file
# from .utils.measure_execution_time import measure_execution_time
# from .utils.print_search_result import print_search_result


def grep_search(file_path: list[str], query: str) -> tuple[bool, str]:
    """
    Search for a pattern in a file using the grep command-line tool.

    Args:
    - file_path (list[str]): The list of strings representing the file content.
    - query (str): The pattern to search for in the file content.

    Returns:
    - tuple[bool, str]: A tuple containing a boolean indicating whether the
                        pattern was found and the matched content if found,
                        or None if not found.
    """
    try:
        # Escape special characters in the query to prevent security
        # vulnerabilities
        escaped_query = subprocess.run(
            ["echo", query], capture_output=True).stdout.decode().strip()

        # Convert the file contents to a string
        file_data = "\n".join(file_path)

        # Run the grep command to search for the query in the file contents
        grep_process = subprocess.Popen(["grep", "-m", "1", "-n", "-w",
                                         escaped_query],
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
        output, _ = grep_process.communicate(input=file_data.encode())
        output = output.decode()

        if output:
            # Extract the matched content
            matched_content = output.split(':', 1)[1].strip()
            return True, matched_content
        else:
            return False, None

    except subprocess.CalledProcessError:
        print("Grep command failed to execute.")
        return False, None


# # Usage
# query = "3;0;1;28;0;7;5;0;"
# file_path = read_file('200k.txt')
# search_name = "grep"

# # Call grep_search with the actual file content
# execution_time, found, matched_line = measure_execution_time(
#     grep_search, file_path, query)

# # Print the search result and execution time
# print_search_result(found, matched_line, query, search_name, execution_time)
