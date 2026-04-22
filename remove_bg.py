import os
from rembg import remove
from PIL import Image

def bg_remove(input_path, output_path):
    print(f"Processing {input_path}...")
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == '__main__':
    bg_remove('assets/60370438.webp', 'assets/60370438_transparent.png')
