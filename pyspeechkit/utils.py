from .exceptions import FileCreationError
from pathlib import Path


def create_voice_file(data: bytes, path: str):
    try:
        with open(Path.cwd() / path, 'wb') as file:
            file.writelines(data)
    except Exception as error:
        raise FileCreationError(error)
