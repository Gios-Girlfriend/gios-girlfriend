import os
import subprocess
from pydub import AudioSegment


def split_vocals(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp3'):
            audio_file = input_path = os.path.join(input_folder, filename)
            # output_path = os.path.join(output_folder,  filename)
            # audio_file = 'audio_example.mp3'
            print(input_path)
            output_dir = output_folder

            subprocess.run(['spleeter', 'separate', '-o', output_dir, audio_file])

        # # audio_file = 'audio_mp3/chirp-1.mp3'
        # # current_vocals_output_file = 'demixed/chirp-1/vocals.wav'
        # # current_accompaniment_output_file = 'demixed/chirp-1/accompaniment.wav'

        # # target_vocals_file = 'demixed/vocals/chirp-1.mp3'
        # # target_accompaniment_file = 'demixed/accompaniment/chirp-1.mp3'

        # vocals_output_file = os.path.join(output_dir, filename, vocals_dir, filename)

        # AudioSegment.from_wav("/input/file.wav").export("/output/file.mp3", format="mp3")

    vocals_dir = "vocals"
    accompaniment_dir = "accompaniment"
    for dir in [vocals_dir, accompaniment_dir]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    # go through the demixed folder, move all the vocals into vocals/
    # go through the demixed folder, move all the accompaniment into accompaniment/

    for dir_name in os.listdir(output_folder):
        for file in os.listdir(os.path.join(output_folder, dir_name)):
            if 'vocals' in file:
                # convert to mp3
                AudioSegment.from_wav(os.path.join(output_folder, dir_name, file)).export(
                    (os.path.join(vocals_dir, dir_name) + ".mp3"), format="mp3")

            elif 'accompaniment' in file:
                AudioSegment.from_wav(os.path.join(output_folder, dir_name, file)).export(
                    (os.path.join(accompaniment_dir, dir_name) + ".mp3"), format="mp3")


if __name__ == "__main__":
    input_folder_path = "audio_mp3"
    output_folder_path = "demixed"

    split_vocals(input_folder_path, output_folder_path)
