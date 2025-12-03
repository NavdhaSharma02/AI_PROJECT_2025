import whisper
import openai
import os
from whisper_cpp_python import Whisper

model_local = whisper.load_model("base")
result_local = model_local.transcribe("audio.wav")
print(result_local["text"])

openai.api_key = os.getenv("OPENAI_API_KEY")
with open("audio.mp3", "rb") as f:
    transcript_api = openai.Audio.transcribe("whisper-1", f)
print(transcript_api["text"])

model_cpp = Whisper(model_path="./models/ggml-base.bin")
output_cpp = model_cpp.transcribe(open("audio.wav", "rb"))
print(output_cpp)
