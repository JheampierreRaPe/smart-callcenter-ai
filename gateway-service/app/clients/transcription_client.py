import httpx

class TranscriptionClient:

    def transcribe(self, audio_file: str):

        response = httpx.post(
            "http://transcription:8001/transcribe",
            json={
                "audio_file": audio_file
            }
        )

        return response.json()
