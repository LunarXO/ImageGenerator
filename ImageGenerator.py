from PIL import Image
import numpy as np
import sys

def make_random_image_fast(width: int, height: int, output_path: str):
    # Random uint8 array: shape (height, width, 3) for RGB
    data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    img = Image.fromarray(data, "RGB")
    img.save(output_path)
    print(f"Saved: {output_path} ({width}x{height})")

if __name__ == "__main__":
    # Usage: python make_random_image_fast.py 1920 1080 out.png
    if len(sys.argv) < 4:
        print("Usage: python make_random_image_fast.py <width> <height> <output.png>")
        sys.exit(1)

    w = int(sys.argv[1])
    h = int(sys.argv[2])
    out = sys.argv[3]

    make_random_image_fast(w, h, out)