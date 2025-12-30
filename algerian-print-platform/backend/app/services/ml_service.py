import os
from PIL import Image, ImageDraw, ImageFont
import uuid

def generate_mock_image(prompt: str) -> str:
    """
    Generates a mock image with the given prompt text.
    Returns the path to the saved image.
    """
    # Create a directory for the images if it doesn't exist
    output_dir = "static/designs"
    os.makedirs(output_dir, exist_ok=True)

    # Create a blank image
    img = Image.new('RGB', (512, 512), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Add the prompt text to the image
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    d.text((10,10), prompt, fill=(0,0,0), font=font)

    # Save the image with a unique filename
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(output_dir, filename)
    img.save(filepath)

    return filepath
