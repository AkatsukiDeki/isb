import json


def read_file(path: str) -> str:
    """The function of reading text from a file
    Args:
      path: the path to the file
    Returns:
      text from the file
    """
    try:
        with open(path, "r", encoding='UTF-8') as file:
            text = file.read()
        return text
    except FileNotFoundError as e:
        print(f"The file was not found: {e}")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")


def write_file(path: str, info: str) -> None:
    """The function of writing information to a file
    Args:
      path: the path to the file
      info: information written to file
    """
    try:
        with open(path, "w", encoding='UTF-8') as file:
            file.write(info)
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}")


def read_json(path: str) -> dict:
    """The function of reading data from a json file
    Args:
      path: the path to the file
    Returns:
      Dictionary with json file structure
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"An error occurred while reading the JSON file: {str(e)}")


def write_json(path: str, info: dict) -> None:
    """The function for writing data to a json file
    Args:
      info: the data to be written to the file
      path: the path to the file
    """
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(info, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing to the file: '{e}'.")
