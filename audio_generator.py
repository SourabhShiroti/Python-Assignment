import pyttsx3

def generate_audio(text, output_path):
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()
    except Exception as e:
        raise RuntimeError(f"Audio generation failed: {e}")

