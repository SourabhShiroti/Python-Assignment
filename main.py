from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

from audio_generator import generate_audio
from image_generator import generate_slide
from video_compiler import compile_video

app = FastAPI()

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class Slide(BaseModel):
    text: str
    image_prompt: str

class VideoRequest(BaseModel):
    title: str
    slides: list[Slide]


@app.post("/generate-video")
def generate_video(data: VideoRequest):
    try:
        slide_assets = []

        for idx, slide in enumerate(data.slides):
            audio_path = f"{OUTPUT_DIR}/audio_{idx}.mp3"
            image_path = f"{OUTPUT_DIR}/slide_{idx}.png"

            generate_audio(slide.text, audio_path)
            generate_slide(data.title, slide.text, image_path)

            slide_assets.append({
                "audio": audio_path,
                "image": image_path
            })

        final_video_path = f"{OUTPUT_DIR}/final_video.mp4"
        compile_video(slide_assets, final_video_path)

        return {
            "status": "success",
            "video_path": final_video_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
