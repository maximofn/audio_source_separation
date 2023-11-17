# Audio source separation

## Introduction

## Installation

Install `ffmpeg`

```bash
sudo apt update
sudo apt install ffmpeg
```

Create a virtual environment

```bash
conda create -y -n audio_separation python=3.11
conda activate audio_separation
```

Install the requirements

```bash
conda install -y pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
conda install -y ipykernel ipywidgets
pip install -r requirements.txt
```