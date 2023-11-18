from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio
import os

pretrained_models = {
    "sepformer-wsj02mix": {
        "source": "speechbrain/sepformer-wsj02mix",
        "savedir": 'pretrained_models/sepformer-wsj02mix',
        "sample_rate": 8000,
    },
    "sepformer-libri2mix": {
        "source": "speechbrain/sepformer-libri2mix",
        "savedir": 'pretrained_models/sepformer-libri2mix',
        "sample_rate": 8000,
    },
    "resepformer-wsj02mix": {
        "source": "speechbrain/resepformer-wsj02mix",
        "savedir": 'pretrained_models/resepformer-wsj02mix',
        "sample_rate": 8000,
    },
}

def separate_audio(audio_file, pretrained_model_name="sepformer-libri2mix", device="cuda"):
    audio, extension = audio_file.split(".")
    audio_name = audio.split("/")[-1]
    pretrained_model = pretrained_models[pretrained_model_name]
    model = separator.from_hparams(source=pretrained_model["source"], savedir=pretrained_model["savedir"], run_opts={"device":device})
    estimated_sources = model.separate_file(path=audio_file)

    separed_audios = []
    for i in range(0, estimated_sources.shape[2]):
        separed_audio = f"{audio_name}_source_{i}.{extension}"
        torchaudio.save(separed_audio, estimated_sources[:, :, i].detach().cpu(), pretrained_model["sample_rate"])
        separed_audios.append(separed_audio)
    
    # remove audio_file
    os.remove(audio_file)
    
    return separed_audios