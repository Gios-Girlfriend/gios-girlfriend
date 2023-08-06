from pydub import AudioSegment
import os
import subprocess


def run_script(script_path, *args):
    cmd = ["python", script_path] + list(args)
    subprocess.run(cmd, check=True)

def apply_mastering(input_audio, equalizer_settings):
    # Apply mastering techniques here
    # Example: Equalization
    eq_audio = input_audio.equalize(bands=[(32, 31), (64, -12), (128, 6), (256, 0), (512, 6), (1024, 0), (2048, -6), (4096, -12)])

    # Example: Compression
    compressed_audio = eq_audio.compress_dynamic_range(threshold=-20.0, ratio=4.0)

    # Example: Limiting
    limited_audio = compressed_audio.max_dBFS(-0.1)

    # Example: Stereo Widening
    widened_audio = limited_audio.pan(-0.2) + limited_audio.pan(0.2)

    return widened_audio

if __name__ == "__main__":
    input_video_folder_path = "videos"
    audio_mp3_output_folder_path = "audio_mp3"
    demixed_output_folder = "demixed"
    vocals_output_folder = "vocals"
    normalised_output_folder = "normalized_music"
    equalized_output_folder = "equalized_music"
    compressed_output_folder = "compressed_music"
    noise_reduced_output_folder = "noise_reduced_music"
    reverb_enhanced_output_folder = "reverb_enhanced_music"
    filtered_output_folder = "filtered_music"
    mastered_output_folder = "mastered_music"
    stitched_output_file = "stitched_audio.mp3"

    # Step 1: Convert MP4 to MP3
    run_script("converter.py", input_video_folder_path, audio_mp3_output_folder_path)
    
    # Step 1.5 split vocals
    run_script("demix.py", audio_mp3_output_folder_path, demixed_output_folder)

    # Step 2: Normalization
    run_script("normalize.py", audio_mp3_output_folder_path, normalised_output_folder)

    # Step 3: Equalization
    run_script("equalize.py", normalised_output_folder, equalized_output_folder)

    # Step 4: Compression and Limiting
    run_script("compression_limiting.py", equalized_output_folder, compressed_output_folder)

    # Step 5: Noise Reduction
    #run_script("denoise.py", compressed_output_folder, noise_reduced_output_folder)

    # Step 6: Reverb Enhancements
    run_script("reverb_enhancing.py", noise_reduced_output_folder, reverb_enhanced_output_folder)

    # Step 7: High-Pass and Low-Pass Filtering
    run_script("hi_lo_pass_filter.py", reverb_enhanced_output_folder, filtered_output_folder)

    # Step 8: Mastering
    for filename in os.listdir(filtered_output_folder):
        if filename.lower().endswith('.mp3'):
            input_path = os.path.join(filtered_output_folder, filename)
            output_path = os.path.join(mastered_output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_mp3(input_path)

            # Apply mastering to the audio
            mastered_audio = apply_mastering(audio, equalizer_settings)

            # Export the mastered audio to the output path
            mastered_audio.export(output_path, format="mp3")

    # Step 9: Stitching
    run_script("stitch.py", mastered_output_folder, stitched_output_file)
