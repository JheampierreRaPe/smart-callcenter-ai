import httpx


class TranscriptionClient:


    def transcribe(self):

        response = httpx.post(
            "http://transcription:8001/transcribe"
        )

        return response.json()
