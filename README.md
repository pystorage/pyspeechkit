pyspeechkit
===
Library for working with a range of technologies for speech recognition and synthesis from Yandex (SpeechKit).

Installation
---
``` shell
pip install pyspeechkit
```

Usage example
---
Yandex SpeechKit requires an API developer key, you can get it [here](https://cloud.yandex.ru/) to use this library.

``` python
from pyspeechkit import TTS


oauth_token = 'your-oauth-token'
folder_id = 'folder-id'

tts = TTS(oauth_token, folder_id)
tts.synthesize(
    text='Hello World. How are you?'
)
tts.save_voice('path/voice.ogg')
```