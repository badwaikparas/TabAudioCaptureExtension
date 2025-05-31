import os
from dotenv import load_dotenv

load_dotenv() 

HUGGINFACE_MODEL_TOKEN = os.getenv("HUGGINFACE_MODEL_TOKEN")

# # instantiate the pipeline
# from pyannote.audio import Pipeline
# pipeline = Pipeline.from_pretrained(
#   "pyannote/speaker-diarization-3.1",
#   use_auth_token=HUGGINFACE_MODEL_TOKEN)

# # run the pipeline on an audio file
# diarization = pipeline("test.wav")

# # dump the diarization output to disk using RTTM format
# with open("audio.rttm", "w") as rttm:
#     diarization.write_rttm(rttm)


# *
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization@2.1",
    use_auth_token=HUGGINFACE_MODEL_TOKEN)

# send pipeline to GPU (when available)
import torch
pipeline.to(torch.device("cuda"))

# apply pretrained pipeline
diarization = pipeline("python backend\\telegramBot\\test.wav")

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
    

# *
# from pyannote.audio import Pipeline
# import torch

# # Use the latest compatible model for pyannote.audio >=3.x
# pipeline = Pipeline.from_pretrained(
#     "pyannote/speaker-diarization",
#     use_auth_token=HUGGINFACE_MODEL_TOKEN
# )

# # Use GPU if available
# pipeline.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# # Run diarization
# diarization = pipeline("python backend\\telegramBot\\test.wav")

# # Print speaker segments
# for turn, _, speaker in diarization.itertracks(yield_label=True):
#     print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")

# with open("audio.rttm", "w") as rttm:
#     diarization.write_rttm(rttm)
