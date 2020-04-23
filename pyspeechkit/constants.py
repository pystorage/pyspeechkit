IAM_API = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
TTS_API = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

RESPONSE_CODES = {
    200: 'Request completed successfully.',
    400: 'The syntax error in the request.',
    401: 'Authorisation Error.',
    429: 'Request limit exceeded.',
    500: 'Server side error.',
    520: 'Unknown Error.'
}
