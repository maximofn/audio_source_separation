import argparse
from video_to_audio import video_to_audio
from separe_audio import separate_audio
from speech_to_text import SST

def main(video_file, transcript_file):
    audio_file = f"{video_file.split('.')[0]}.wav"
    print(f"Converting {video_file} to {audio_file}")
    video_to_audio(video_file, audio_file)

    print(f"\nSeparating {audio_file} to 2 audios")
    separed_audios = separate_audio(audio_file)

    print(f"\nTranscribing {separed_audios[1]}")
    transcript = SST(separed_audios[1])

    print(f"\nSaving transcript to {transcript_file}")
    with open(transcript_file, "w") as f:
        f.write(transcript["text"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_file", help="input video file", required=True)
    parser.add_argument("--transcript_file", help="output transcript file", required=True)
    args = parser.parse_args()

    main(args.video_file, args.transcript_file)