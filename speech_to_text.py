import whisper
import os

def SST(audio, whisper_model="large-v3", device='cuda'):
    """
    Speech to text

    Args:
        audio (str): input audio file
        whisper_model (str): whisper model name
        device (str): device to use

    Returns:
        dict: dict of transcript
    """
    model = whisper.load_model(whisper_model, device=device)
    result = model.transcribe(audio, word_timestamps=True)
    os.remove(audio)
    return result