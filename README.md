pyspeechkit ![Twitter Follow](https://img.shields.io/twitter/follow/thePystorage?label=pystorage&style=social)
===
Library for working with a range of technologies for speech recognition and synthesis from Yandex (SpeechKit).

![PyPI](https://img.shields.io/pypi/v/pyspeechkit)
[![Downloads](https://pepy.tech/badge/pyspeechkit)](https://pepy.tech/project/pyspeechkit)
![GitHub](https://img.shields.io/github/license/pystorage/pyspeechkit)

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
