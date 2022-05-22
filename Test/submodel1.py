from deepspeech import Model
import numpy as np
import os
import wave

from IPython.display import Audio

model_file_path = 'deepspeech-0.9.3-models.pbmm'
lm_file_path = 'deepspeech-0.9.3-models.scorer'
beam_width = 100
lm_alpha = 0.93
lm_beta = 1.18

model = Model(model_file_path)
model.enableExternalScorer(lm_file_path)

def read_wav_file(filename):
    with wave.open(filename, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)

    return buffer, rate



stream = model.createStream()

from IPython.display import clear_output

def transcribe_streaming(audio_file):
    buffer, rate = read_wav_file(audio_file)
    offset=0
    batch_size=8196
    text=""

    while offset < len(buffer):
      end_offset=offset+batch_size
      chunk=buffer[offset:end_offset]
      data16 = np.frombuffer(chunk, dtype=np.int16)

      stream.feedAudioContent(data16)
      text=stream.intermediateDecode()
      clear_output(wait=True)
      offset=end_offset
    return text




