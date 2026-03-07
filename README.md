# AI Video Dubbing Pipeline

This project implements an automated AI pipeline that converts a training video into a Hindi dubbed version. The system extracts audio from a video, transcribes the speech, translates it to Hindi, generates Hindi speech, and finally synchronizes the video with the new audio.

The goal of this project is to demonstrate a **high-quality AI dubbing system while minimizing infrastructure cost**, using open-source tools and efficient pipeline design.

---

# Pipeline Overview

The pipeline processes a video through multiple stages:

Input Video  
↓  
Clip Extraction (FFmpeg)  
↓  
Audio Extraction (FFmpeg)  
↓  
Silence Detection & Audio Segmentation  
↓  
Speech Recognition (Sarvam ASR)  
↓  
Translation (Sarvam Translation)  
↓  
Hindi Voice Generation (Sarvam TTS)  
↓  
Lip Sync Generation (SadTalker)  
↓  
Final Hindi Dubbed Video

The system is designed in a **modular architecture**, allowing each component to be replaced or improved independently.

---

# Project Structure
ai-video-dubbing-pipeline
│
├── modules
│ ├── extract_clip.py
│ ├── extract_audio.py
│ ├── transcribe.py
│ ├── translate.py
│ ├── generate_voice.py
│ ├── merge_audio_video.py
│ └── audio_segment.py
│
├── input
│ └── video.mp4
│
├── outputs
│ ├── clip.mp4
│ ├── audio.wav
│ ├── hindi_audio.wav
│ └── dubbed_video.mp4
│
├── dub_video.py
├── requirements.txt


---

# Setup Instructions

### 1. Clone Repository
git clone https://github.com/YOUR\_USERNAME/ai-video-dubbing-pipeline.git

cd ai-video-dubbing-pipeline

### 2. Create Virtual Environment

python -m venv .venv


Activate environment:

Windows
.venv\Scripts\activate


Mac/Linux
source .venv/bin/activate

---

### 3. Install Dependencies


pip install -r requirements.txt


---

### 4. Install FFmpeg

Download from:


https://ffmpeg.org/download.html


Ensure it is available in your system PATH.

---

### 5. Add API Key

Add your Sarvam API key in:


modules/transcribe.py
modules/generate_voice.py
modules/translate.py


---

### 6. Run Pipeline

Place the source video in:


input/video.mp4


Then run:



python dub_video.py


Output will be saved in:


outputs/dubbed_video.mp4


---

# Dependencies

Main dependencies used in this project:

Python Libraries


requests
pydub
ffmpeg-python


External Tools


FFmpeg
Sarvam AI APIs
SadTalker (for lip synchronization)


---
## SadTalker External Dependencies

SadTalker is used in this project to generate lip-synced video from the Hindi audio.  
It requires additional deep learning libraries and pretrained models.

---

### 1. Python Dependencies

SadTalker requires the following Python packages:


torch
torchvision
torchaudio
numpy
scikit-image
opencv-python
facexlib
kornia
yacs
gfpgan
basicsr


Example installation:


pip install torch torchvision torchaudio
pip install numpy opencv-python scikit-image
pip install facexlib kornia yacs gfpgan basicsr
### 2. FFmpeg

SadTalker relies on FFmpeg for video processing.

Install from:

https://ffmpeg.org/download.html

Verify installation:

ffmpeg -version

### 3. GPU Support (Recommended)


SadTalker performs best when running on GPU.

Recommended configuration:

NVIDIA GPU

CUDA 11+

Example PyTorch installation with CUDA:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

SadTalker can run on CPU, but processing will be significantly slower.

### 4. SadTalker Model Checkpoints

The following pretrained models are required:

epoch_20.pth
SadTalker\_V0.0.2\_256.safetensors  
mapping\_00229-model.pth.tar  


Place them inside:


SadTalker/checkpoints/


These models are used for:

facial animation

expression modeling

lip synchronization

### 5. Running SadTalker

Example command:

cd SadTalker 
python inference.py --driven_audio ../outputs/hindi_audio.wav --source_image ../outputs/new_frame.jpg --result_dir ../outputs --preprocess full --enhancer gfpgan
ffmpeg -i "../outputs/2026_03_05_20.54.20.mp4" -i "../outputs/hindi_audio.wav" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest "../outputs/final_dubbed_video.mp4"

# Estimated Cost if Scaled

This prototype is designed to run at **minimal cost** using open-source tools and efficient processing.

Approximate cost estimation:

| Component | Cost |
|--------|--------|
Speech Recognition | Free tier / minimal API cost |
Translation | Free tier |
Voice Generation | Minimal API cost |
Video Processing | Free (FFmpeg) |
Lip Sync | GPU compute |

Estimated cost per minute of video:


$0.02 – $0.05 per minute


If scaled using GPU instances:


~$10 to process 500 hours of video overnight
(using distributed GPU workers)


This makes the pipeline economically viable for startups.

---

# Known Limitations

Current prototype limitations include:

1. Lip sync quality depends on the reference frame quality.
2. Audio timing alignment is basic and could be improved with phoneme alignment.
3. Translation may occasionally produce literal phrases rather than conversational Hindi.
4. The current implementation processes segments sequentially rather than fully parallelized.

---

# Improvements with More Time

With additional time and resources, the following improvements could be implemented:

### 1. Phoneme-Level Lip Sync
Using models such as **Wav2Lip or VideoReTalking** for more precise mouth movements.

### 2. Parallel Processing
Implement distributed processing using:

- Celery workers
- Redis queues
- Kubernetes GPU nodes

This would enable processing **hundreds of hours of video overnight**.

### 3. Better Voice Cloning
Using advanced models such as:

- XTTS v2
- ElevenLabs
- Bark

for more natural speech.

### 4. Automatic Subtitle Alignment
Generate timestamps and subtitles to improve dubbing synchronization.

### 5. Full-Length Video Support
Improve batching and segment merging for long-form video processing.

---

# Future Architecture (Scaling)

To scale the system for large datasets:

Video Dataset
↓
Video Segmentation
↓
Distributed Workers (GPU)
↓
ASR → Translation → TTS
↓
Lip Sync
↓
Video Assembly


This architecture would allow the system to process **500+ hours of video overnight**.

---

# Output

Example output:


outputs/final_dubbed_video.mp4


A Hindi dubbed version of the selected video segment with synchronized lip movements.

---

# Author

Harish D
AI/ML Developer
