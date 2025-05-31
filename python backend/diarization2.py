import requests
import time

import os
from dotenv import load_dotenv

load_dotenv() 
ASSEMBLY_AI_TOKEN = os.getenv("ASSEMBLY_AI_TOKEN")


base_url = "https://api.assemblyai.com"

headers = {
    "authorization": ASSEMBLY_AI_TOKEN
}

with open("./python backend/test.wav", "rb") as f:
  response = requests.post(base_url + "/v2/upload",
                          headers=headers,
                          data=f)

upload_url = response.json()["upload_url"]

data = {
    "audio_url": upload_url, # You can also use a URL to an audio or video file on the web
    "speaker_labels": True
}

url = base_url + "/v2/transcript"
response = requests.post(url, json=data, headers=headers)

transcript_id = response.json()['id']
polling_endpoint = base_url + "/v2/transcript/" + transcript_id

while True:
  transcription_result = requests.get(polling_endpoint, headers=headers).json()

  if transcription_result['status'] == 'completed':
    print(f"Transcript ID:", transcript_id)
    break

  elif transcription_result['status'] == 'error':
    raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

  else:
    time.sleep(3)

for utterance in transcription_result['utterances']:
  print(f"Speaker {utterance['speaker']}: {utterance['text']}")
