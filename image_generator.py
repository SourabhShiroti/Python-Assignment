from PIL import Image, ImageDraw, ImageFont
import textwrap

WIDTH, HEIGHT = 1280, 720


def generate_slide(title, text, output_path):
    try:
        img = Image.new("RGB", (WIDTH, HEIGHT), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

        draw.text((50, 40), title, fill="black", font=title_font)

        wrapped_text = textwrap.fill(text, width=60)
        draw.text((50, 150), wrapped_text, fill="black", font=body_font)

        img.save(output_path)
    except Exception as e:
        raise RuntimeError(f"Image generation failed: {e}")

