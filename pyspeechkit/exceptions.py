from .constants import RESPONSE_CODES


class Error(Exception):
    pass


class RequestError(Error):
    pass


class FileError(Error):
    pass


class ApiRequestError(RequestError):
    def __init__(self, message: str):
        super().__init__(f'ApiRequestError: {message}')
        self.message = message


class TokenRequestError(RequestError):
    def __init__(self, code: int):
        message = RESPONSE_CODES[code]
        super().__init__(f'TokenRequestError: {code} - {message}')
        self.code = code
        self.message = message


class TTSRequestError(RequestError):
    def __init__(self, code: int):
        message = RESPONSE_CODES[code]
        super().__init__(f'TTSRequestError: {code} - {message}')
        self.code = code
        self.message = message


class FileCreationError(FileError):
    def __init__(self, message: str):
        super().__init__(f'FileCreationError: {message}')
        self.message = message
