from pydub import AudioSegment
import os

def normalize_volume(input_folder, output_folder, target_dBFS=-20.0):
    print("Normalize")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_mp3(input_path)

            # Normalize the audio to the target dBFS level
            normalized_audio = audio.apply_gain(target_dBFS - audio.dBFS)

            # Export the normalized audio to the output folder
            normalized_audio.export(output_path, format="mp3")
