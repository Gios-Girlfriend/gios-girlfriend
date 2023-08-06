import os
import subprocess

def run_script(script_path, *args):
    cmd = ["python", script_path] + list(args)
    subprocess.run(cmd, check=True)

def apply_mastering(input_path, output_path):
    # Apply mastering techniques here
    # Example: Equalization
    eq_audio = audio.equalize(bands=[(32, 31), (64, -12), (128, 6), (256, 0), (512, 6), (1024, 0), (2048, -6), (4096, -12)])

    # Example: Compression
    compressed_audio = eq_audio.compress_dynamic_range(threshold=-20.0, ratio=4.0)

    # Example: Limiting
    limited_audio = compressed_audio.max_dBFS(-0.1)

    # Example: Stereo Widening
    widened_audio = limited_audio.pan(-0.2) + limited_audio.pan(0.2)

    # Export the mastered audio to the output path
    widened_audio.export(output_path, format="mp3")

if __name__ == "__main__":
    input_folder_path = "music"
    normalised_output_folder = "normalised_music"
    equalized_output_folder = "equalized_music"
    compressed_output_folder = "compressed_music"
    noise_reduced_output_folder = "noise_reduced_music"
    reverb_enhanced_output_folder = "reverb_enhanced_music"
    filtered_output_folder = "filtered_music"
    mastered_output_folder = "mastered_music"
    stitched_output_file = "stitched_audio.mp3"

    # Step 1: Normalization
    run_script("normalise.py", input_folder_path, normalised_output_folder)

    # Step 2: Equalization
    run_script("equalize.py", normalised_output_folder, equalized_output_folder)

    # Step 3: Compression and Limiting
    run_script("compression_limiting.py", equalized_output_folder, compressed_output_folder)

    # Step 4: Noise Reduction
    run_script("noise_reduction.py", compressed_output_folder, noise_reduced_output_folder)

    # Step 5: Reverb Enhancements
    run_script("reverb_enhancements.py", noise_reduced_output_folder, reverb_enhanced_output_folder)

    # Step 6: High-Pass and Low-Pass Filtering
    run_script("high_low_pass_filter.py", reverb_enhanced_output_folder, filtered_output_folder)

    # Step 7: Mastering
    for filename in os.listdir(filtered_output_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(filtered_output_folder, filename)
            output_path = os.path.join(mastered_output_folder, filename)

            apply_mastering(input_path, output_path)

    # Step 8: Stitching
    run_script("stitch.py", mastered_output_folder, stitched_output_file)
