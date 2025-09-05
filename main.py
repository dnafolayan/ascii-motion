from PIL import Image
import argparse
import os
import sys


def validate_path(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist")
        sys.exit(1)

    if not os.path.isfile(path):
        print(f"Path '{path}' is not a file")
        sys.exit(1)

    if not path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
        print(f"Path '{path}' is not a valid image file")
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument("-p", "--path", type=str, required=True, help="Path to the image file")

    args = parser.parse_args()
    validate_path(args.path)

    return args


def load_img():
    args = parse_args()
    img = Image.open(args.path)

    return img


def resize_img(img, target_width=100):
    w, h = img.size
    aspect_ratio = h / w

    new_height = int(target_width * aspect_ratio * 0.55)
    resized_img = img.resize((target_width, new_height))

    return resized_img


def to_grayscale(img):
    gray_img = img.convert("L")

    return gray_img

def map_brightness(img):
    ascii_chars = '@%#*+=-:. '
    # ascii_chars = ascii_chars[::-1]

    pixels = img.getdata()
    w, _ = img.size

    row_idx = 0
    ascii_img = ''

    for pixel in pixels:
        ascii_chars_idx = pixel * (len(ascii_chars) - 1) // 255
        ascii_char = ascii_chars[ascii_chars_idx] 

        ascii_img = ascii_img + ascii_char 

        row_idx += 1
        
        if row_idx == w:
            ascii_img = ascii_img + '\n'
            row_idx = 0

    return ascii_img


def main():
    try:
        img = load_img()
    except Exception:
        print("Failed to load Image")
        return

    print(map_brightness(to_grayscale(resize_img(img))))


if __name__ == "__main__":
    main()
