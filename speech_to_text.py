import whisper

def SST(audio, whisper_model="large-v3", device='cuda'):
    model = whisper.load_model(whisper_model, device=device)
    result = model.transcribe(audio, word_timestamps=True)
    return result