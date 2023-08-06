from pydub import AudioSegment, effects  

rawsound = AudioSegment.from_file("./input.mp3", "mp3")  
normalizedsound = effects.normalize(rawsound)  
normalizedsound.export("./output.mp3", format="mp3")