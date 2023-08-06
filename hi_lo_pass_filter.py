from pydub import AudioSegment
import os

def apply_high_low_pass_filter(input_folder, output_folder, high_pass_cutoff=1000, low_pass_cutoff=10000):
    print("Hi Low Pass Filter")
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_file(input_path)

            # Apply high-pass filter
            high_pass_filtered_audio = audio.high_pass_filter(high_pass_cutoff)

            # Apply low-pass filter
            low_pass_filtered_audio = high_pass_filtered_audio.low_pass_filter(low_pass_cutoff)

            # Export the filtered audio to the output folder
            low_pass_filtered_audio.export(output_path, format="mp3")
