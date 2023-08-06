from pydub import AudioSegment
import os

def apply_compression_limiting(input_folder, output_folder, threshold=-20.0, ratio=4.0, attack=10, release=200):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_file(input_path)

            # Apply compression and limiting
            compressed_audio = audio.compress_dynamic_range(threshold=threshold, ratio=ratio, attack=attack, release=release)

            # Export the processed audio to the output folder
            compressed_audio.export(output_path, format="mp3")
