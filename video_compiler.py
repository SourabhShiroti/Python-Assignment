from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


def compile_video(slides, output_path):
    clips = []
    try:
        for slide in slides:
            audio = AudioFileClip(slide['audio'])
            image = ImageClip(slide['image']).set_duration(audio.duration)
            image = image.set_audio(audio)
            clips.append(image)

        final_video = concatenate_videoclips(clips, method="compose")
        final_video.write_videofile(output_path, fps=24)
    except Exception as e:
        raise RuntimeError(f"Video compilation failed: {e}")

