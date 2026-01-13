# Media Automation Pipeline

A Python application that generates atomic media assets (audio + slides/images) from structured input and compiles them into a final video output.

## Features

- **Audio Generation**: Converts slide text to speech using gTTS (Google Text-to-Speech)
- **Image Generation**: Creates slide images with title and text content
- **Video Compilation**: Combines images and audio into a final MP4 video
- **REST API**: FastAPI endpoint for video generation

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. **Install FFmpeg** (required for video processing):
   - **Windows**: Download from https://ffmpeg.org/download.html and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg` or `sudo yum install ffmpeg`

**Note**: This application requires an internet connection for TTS (Text-to-Speech) generation.

## Usage

### Start the API Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Endpoint

**POST /generate-video**

Request body:
```json
{
  "title": "Introduction to Photosynthesis",
  "slides": [
    {
      "text": "Photosynthesis is the process by which plants make food.",
      "image_prompt": "green plants under sunlight"
    },
    {
      "text": "It uses sunlight, carbon dioxide, and water.",
      "image_prompt": "diagram of photosynthesis process"
    }
  ]
}
```

Response:
```json
{
  "status": "success",
  "video_path": "output/final_video.mp4"
}
```

### Example Request

Using curl:
```bash
curl -X POST "http://localhost:8000/generate-video" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Introduction to Photosynthesis",
    "slides": [
      {
        "text": "Photosynthesis is the process by which plants make food.",
        "image_prompt": "green plants under sunlight"
      },
      {
        "text": "It uses sunlight, carbon dioxide, and water.",
        "image_prompt": "diagram of photosynthesis process"
      }
    ]
  }'
```

## Project Structure

- `audio_generator.py`: Handles text-to-speech audio generation
- `image_generator.py`: Creates slide images with title and text
- `video_compiler.py`: Combines images and audio into video
- `main.py`: FastAPI application with REST endpoints
- `requirements.txt`: Python dependencies

## Output

Generated files are saved in the `output/` directory:
- `output/audio/`: Generated audio files (MP3)
- `output/images/`: Generated slide images (PNG)
- `output/final_video.mp4`: Final compiled video

