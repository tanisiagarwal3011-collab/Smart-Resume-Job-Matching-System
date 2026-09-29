import os
def validate_file(file_path):
    """
    Check whether a file exists and is accessible.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Required file not found: {file_path}"
        )
    if not os.path.isfile(file_path):
        raise ValueError(
            f"Path is not a valid file: {file_path}"
        )
    return True
def read_text_file(file_path):
    """
    Read and return the contents of a text file.
    """
    validate_file(file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
def validate_text(text, field_name="Text"):
    """
    Validate that text input is not empty.
    """
    if not text or not text.strip():
        raise ValueError(
            f"{field_name} cannot be empty."
        )
    return True
def format_percentage(value, decimal_places=2):
    """
    Format a numeric value as a percentage string.
    """
    return f"{value:.{decimal_places}f}%"
if __name__ == "__main__":
    test_file = "job.txt"
    try:
        validate_file(test_file)
        content = read_text_file(test_file)
        validate_text(content, "Job Description")
        print("Utils module test successful!")
        print()
        print("Job description loaded successfully.")
        print()
        print("Formatted percentage:", format_percentage(61.1111))
    except (FileNotFoundError, ValueError) as error:
        print("Error:", error)
