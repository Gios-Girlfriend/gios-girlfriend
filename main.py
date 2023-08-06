import os
import subprocess

def run_script(script_path, *args):
    cmd = ["python", script_path] + list(args)
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    input_folder = "music"
    normalised_output_folder = "normalised_music"
    equalized_output_folder = "equalized_music"
    stitched_output_file = "stitched_audio.mp3"

    # Execute the normalization script
    run_script("normalise.py", input_folder, normalised_output_folder)

    # Execute the equalization script
    run_script("equalize.py", normalised_output_folder, equalized_output_folder)

    # Execute the stitching script
    run_script("stitch.py", equalized_output_folder, stitched_output_file)