from pydub import AudioSegment
import os

def apply_equalization(audio, equalizer_settings):
    for freq, gain in equalizer_settings:
        band = audio.high_pass_filter(freq) - audio.low_pass_filter(freq)
        audio = audio.overlay(band + gain)

    return audio

def equalize_mp3_files(input_folder, output_folder, equalizer_settings):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_mp3(input_path)

            # Apply equalization to the audio
            equalized_audio = apply_equalization(audio, equalizer_settings)

            # Export the equalized audio to the output folder
            equalized_audio.export(output_path, format="mp3")

if __name__ == "__main__":
    # Define the folder to operate in as 'music'
    input_folder_path = "normalized_music"
    output_folder_path = "equalized_music"

    # Set equalizer settings (Example: boosting 2kHz by 6dB)
    equalizer_settings = [{"frequency": 2000, "gain": 6.0}]
    
    equalize_mp3_files(input_folder_path, output_folder_path, equalizer_settings)