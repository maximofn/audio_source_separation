# Audio source separation

## Introduction

This repository contains the code for the audio source separation project. The goal of this project is to separate the vocals from a video, and trascribe the vocals to text.

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

## Usage

To execute the code, run the following command:

```bash
python main.py --video_file [video_file] --transcript_file [transcription_file]
```
