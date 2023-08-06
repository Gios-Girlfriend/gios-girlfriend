from pydub import AudioSegment


sound1 = AudioSegment.from_file("audio/biden_rebuttal.mp3")
sound2 = AudioSegment.from_file("audio/Spectre.mp3")

# Get loudness of each audio file
sound1_dBFS = sound1.dBFS
sound2_dBFS = sound2.dBFS

# Equalize loudness
if sound1_dBFS > sound2_dBFS:
  sound1 = sound1.apply_gain(sound2_dBFS - sound1_dBFS)
else:
  sound2 = sound2.apply_gain(sound1_dBFS - sound2_dBFS)

# Overlay audio files  
combined = sound1.overlay(sound2) 

# Export combined audio
combined.export("audio/combined_equalized.mp3", format='mp3')