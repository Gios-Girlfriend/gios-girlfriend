from pydub import AudioSegment
import os

def apply_reverb_enhancements(input_folder, output_folder, reverb_duration=500, reverb_decay=0.5):
    print("reverb enhancements")
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_file(input_path)

            # Apply reverb enhancements
            reverb_enhanced_audio = audio.overlay(audio * reverb_decay, position=reverb_duration)

            # Export the reverb-enhanced audio to the output folder
            reverb_enhanced_audio.export(output_path, format="mp3")
