import json


class Work:
    def __init__(self):
        pass

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
            print(f"Непредвиденная ошибка: {str(e)}")

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
            print(f"Ошибка! Файл {path} не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

    def read_bytes(path: str) -> bytes:
        """
        Reads the contents of a file in binary format.
        Args:
            path: The path to the file to be read.
        Returns:
            The contents of the file in binary format.
        """
        try:
            with open(path, "rb") as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"Ошибка! Файл {path} не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

    def read_bytes_from_text(path: str) -> bytes:
        """
        Reads the bytes contents of a file in text format.
        Args:
            path: The path to the file to be read.
        Returns:
            The contents of the file in binary format.
        """
        try:
            with open(path, "r", encoding='UTF-8') as file:
                text = file.read()
            return text.encode('utf-8')
        except FileNotFoundError:
            print(f"Ошибка! Файл {path} не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")

    def write_bytes_text(path: str, bytes_text: bytes) -> None:
        """
        Writes binary data to a file.
        Args:
            path: The path to the file where the data will be written.
            bytes_text: The binary data to be written to the file.
        """
        try:
            with open(path, "wb") as file:
                file.write(bytes_text)
        except FileNotFoundError:
            print(f"Ошибка! Файл {path} не найден.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")
