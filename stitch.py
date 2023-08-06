from pydub import AudioSegment
import os

def append_mp3_files(input_folder, output_filename):
    # Create an empty AudioSegment to hold the concatenated audio
    concatenated_audio = AudioSegment.empty()

    # Get a list of MP3 files in the input folder
    mp3_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.mp3')]

    # Sort the list of MP3 files in alphabetical order
    mp3_files.sort()

    for filename in mp3_files:
        file_path = os.path.join(input_folder, filename)

        # Load each MP3 file
        audio = AudioSegment.from_mp3(file_path)

        # Append the loaded audio to the concatenated_audio
        concatenated_audio += audio

    # Export the concatenated audio as a single MP3 file
    concatenated_audio.export(output_filename, format="mp3")

if __name__ == "__main__":
    # Define the folder to operate in as 'music'
    input_folder_path = "equalized_music"

    # Define the output filename for the concatenated audio
    output_filename = "concatenated_audio.mp3"
    
    append_mp3_files(input_folder_path, output_filename)
