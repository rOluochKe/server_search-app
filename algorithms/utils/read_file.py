def read_file(filename: str) -> list[str]:
    """
    Reads the contents of a file and returns a list of lines.

    Args:
        filename (str): The path to the file to read.

    Returns:
        list[str]: A list containing the lines from the file, or None if an
                   error occurs.

    Raises:
        ValueError: If the provided filename is not a string.
    """
    if not isinstance(filename, str):
        raise ValueError("filename must be a string")

    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None
