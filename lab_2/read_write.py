import json


def write_file(path: str, info: str) -> None:
    """The function of writing information to a file
    Args:
      path: the path to the file
      info: information written to file
    """
    try:
        with open(path, "a+", encoding='UTF-8') as file:
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