import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp4'):
            input_path = os.path.join(input_folder, filename)

            # Load the video clip
            video_clip = VideoFileClip(input_path)

            # Get the audio part of the clip
            audio_clip = video_clip.audio

            # Create the output filename by replacing the extension with .mp3
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(output_folder, output_filename)

            # Export the audio as an MP3 file
            audio_clip.write_audiofile(output_path)

            # Close the video clip to release resources
            video_clip.close()

if __name__ == "__main__":
    # Replace 'input_folder_path' and 'output_folder_path' with your desired paths
    input_folder_path = "videos"
    output_folder_path = "audio_mp3"

    convert_mp4_to_mp3(input_folder_path, output_folder_path)
