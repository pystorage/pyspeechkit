from .constants import IAM_API, TTS_API
from .exceptions import ApiRequestError, TokenRequestError, TTSRequestError
import json
import requests


class API:
    def __init__(self, oauth_token: str):
        self.oauth_token = oauth_token

    def request(self, url: str, data: str, headers: dict = None):
        try:
            with requests.post(url, data, headers=headers) as response:
                return response
        except Exception as error:
            raise ApiRequestError(error)

    def generate_token(self):
        data = {'yandexPassportOauthToken': self.oauth_token}
        response = self.request(IAM_API, json.dumps(data))
        if response.status_code == 200:
            return response.json()['iamToken']
        else:
            raise TokenRequestError(response.status_code)

    def tts_request(self, data: dict):
        headers = {'Authorization': f'Bearer {self.generate_token()}'}
        response = self.request(TTS_API, data, headers)
        if response.status_code == 200:
            return response
        else:
            raise TTSRequestError(response.status_code)
