import argparse
from video_to_audio import video_to_audio
from separe_audio import separate_audio
from speech_to_text import SST

def main(video_file, transcript_file, separe_vocal=False):
    """
    Main function

    Args:
        video_file (str): input video file
        transcript_file (str): output transcript file

    Returns:
        None
    """
    audio_file = f"{video_file.split('.')[0]}.wav"
    print(f"Converting {video_file} to {audio_file}")
    video_to_audio(video_file, audio_file)

    if separe_vocal:
        print(f"\nSeparating {audio_file} to 2 audios")
        separed_audios = separate_audio(audio_file)
    else:
        separed_audios = [audio_file]

    if separe_vocal:
        i = 0
    else:
        i = 0
    print(f"\nTranscribing {separed_audios[i]}")
    transcript = SST(separed_audios[i])

    print(f"\nSaving transcript to {transcript_file}")
    if separe_vocal:
        transcript_file = f"{transcript_file.split('.')[0]}_vocals.{transcript_file.split('.')[1]}"
    with open(transcript_file, "w") as f:
        f.write(transcript["text"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_file", help="input video file", required=True)
    parser.add_argument("--transcript_file", help="output transcript file", required=True)
    parser.add_argument("--separe_vocal", help="separe vocal from audio", action="store_true")
    args = parser.parse_args()

    main(args.video_file, args.transcript_file, args.separe_vocal)