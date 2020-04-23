from .api import API
from .utils import create_voice_file


class TTS(API):
    def __init__(self, oauth_token: str, folder_id: str):
        super().__init__(oauth_token)
        self.folder_id = folder_id

    def synthesize(self, **parameters: str):
        try:
            parameters.update({'folderId': self.folder_id})
            self.synthesized = super().tts_request(parameters)
        except Exception as error:
            print(error)

    def voice_source(self):
        return self.synthesized

    def save_voice(self, path: str):
        try:
            create_voice_file(self.synthesized, path)
        except Exception as error:
            print(error)
