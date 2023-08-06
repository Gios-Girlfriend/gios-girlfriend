import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import librosa
import pydub
import soundfile as sf


sample_rate = 44100
duration = 5  # seconds


def sine_tone(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(duration*sample_rate))
    vibrato_freq = 5  # Hz
    vibrato_amp = 2  # Hz
    tone = np.sin(2*np.pi * (frequency + vibrato_amp *
                  np.sin(2*np.pi*vibrato_freq*t)) * t)
    return tone


def create_melody(notes, durations, sample_rate):
    audio = np.array([])
    for n, d in zip(notes, durations):
        harmony = [n, n+4, n+7]
        for note in harmony:
            tone = sine_tone(note, d, sample_rate)
            audio = np.append(audio, tone)
    return audio.astype(np.int16)


def main():
    input_file = "audio/biden_rebuttal.mp3"
    output_file = "audio/output.wav"  # librosa outputs .wav files

    # C D E F G A B C    durations = [0.5, 0.5, 0.5, 0.5, 1, 0.5]
    notes = [261, 293, 329, 349, 391, 440, 493, 523]
    durations = [0.25, 0.5, 1, 0.25, 0.5, 0.25, 0.5, 1]

    # Load the audio file with librosa
    y, sr = librosa.load(input_file, sr=None)

    # Calculate total duration of melody
    total_duration = sum(durations)

    # Calculate number of samples per segment
    samples_per_segment = int(len(y) / total_duration)

    # Split audio into segments
    segments = [y[i:i+samples_per_segment]
                for i in range(0, len(y), samples_per_segment)]

    # Match number of segments to number of notes
    segments = segments[:len(notes)]

    # Pitch shift each segment
    shifted_segments = []
    for i, segment in enumerate(segments):
        # Shift pitch to match corresponding note
        # We'll use a dummy pitch shifting here, as real pitch shifting would require more complex calculations
        n_steps =  notes[i] - notes[0]
        shifted_segment = librosa.effects.pitch_shift(segment, sr=sr, n_steps=n_steps)

        shifted_segments.append(shifted_segment)

    # Concatenate segments back together
    y_shifted = np.concatenate(shifted_segments)

    # Save the output
    sf.write(output_file, y_shifted, sr)


if __name__ == "__main__":
    main()
