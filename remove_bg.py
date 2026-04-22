import os
import sys
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
    bg_remove('assets/zinc.png', 'assets/zinc_transparent.png')
    bg_remove('assets/metal.png', 'assets/metal_transparent.png')
    bg_remove('assets/tile.png', 'assets/tile_transparent.png')
    bg_remove('assets/60392108.webp', 'assets/60392108_transparent.png')
