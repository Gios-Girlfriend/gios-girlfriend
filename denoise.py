import os
import noisereduce as nr
import numpy as np
from pydub import AudioSegment

def apply_noise_reduction(input_folder, output_folder, reduction_strength=0.5):
    print("Denoise")
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_file(input_path)

            # Convert the audio to a NumPy array
            samples = np.array(audio.get_array_of_samples())

            # Perform noise reduction
            reduced_noise = nr.reduce_noise(audio_clip=samples, noise_clip=samples[:10000], verbose=False)

            # Convert the reduced audio back to AudioSegment
            reduced_audio = AudioSegment(
                reduced_noise.tobytes(),
                frame_rate=audio.frame_rate,
                sample_width=reduced_noise.dtype.itemsize,
                channels=audio.channels
            )

            # Export the reduced audio to the output folder
            reduced_audio.export(output_path, format="mp3")

if __name__ == "__main__":
    # Replace 'input_folder_path' and 'output_folder_path' with your desired paths
    input_folder_path = "compressed_music"
    output_folder_path = "noise_reduced_music"

    # Adjust the reduction_strength parameter (0.0 to 1.0) based on the noise level
    reduction_strength = 0.5

    apply_noise_reduction(input_folder_path, output_folder_path, reduction_strength)
