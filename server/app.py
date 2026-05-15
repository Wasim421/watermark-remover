from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse

from TTS.api import TTS

import shutil

app = FastAPI()

tts = TTS(
"tts_models/multilingual/multi-dataset/xtts_v2"
)

@app.post("/generate")
async def generate(
text: str = Form(...),
voice: UploadFile = None
):

    with open("voice.wav","wb") as f:
        shutil.copyfileobj(voice.file,f)

    tts.tts_to_file(
        text=text,
        speaker_wav="voice.wav",
        language="bn",
        file_path="output.wav"
    )

    return FileResponse("output.wav")
