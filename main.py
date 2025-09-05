from PIL import Image
import cv2
import argparse
import time
import os
import sys


def validate_path(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist")
        sys.exit(1)

    if not os.path.isfile(path):
        print(f"Path '{path}' is not a file")
        sys.exit(1)

    if not path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        print(f"File '{path}' is not a supported video format")
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument("-p", "--path", type=str, required=True, help="Path to the image file")

    args = parser.parse_args()
    validate_path(args.path)

    return args


def resize_frame(img, target_width=100):
    w, h = img.size
    aspect_ratio = h / w

    new_height = int(target_width * aspect_ratio * 0.55)
    resized_frame = img.resize((target_width, new_height))

    return resized_frame


def to_grayscale(frame):
    gray_frame = frame.convert("L")

    return gray_frame

def map_brightness(frame):
    ascii_chars = "@%#*+=-:. "
    # ascii_chars = ascii_chars[::-1]

    pixels = frame.getdata()
    w, _ = frame.size

    row_idx = 0
    ascii_str = ''

    for pixel in pixels:
        ascii_chars_idx = pixel * (len(ascii_chars) - 1) // 255
        ascii_char = ascii_chars[ascii_chars_idx] 

        ascii_str = ascii_str + ascii_char

        row_idx += 1
        
        if row_idx == w:
            ascii_str = ascii_str + '\n'
            row_idx = 0

    return ascii_str


def frame_to_ascii(frame, width=100):
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    img = resize_frame(img, target_width=width)
    img = to_grayscale(img)

    ascii_str = map_brightness(img)
    return ascii_str

def play_vid(path):
    try:
        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS)

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            ascii_frame = frame_to_ascii(frame)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_frame)

            time.sleep(1 / fps)
    except KeyboardInterrupt:
        print("Video playback interrupted.")
    finally:
        cap.release()


def main():
    args = parse_args()
    play_vid(args.path)


if __name__ == "__main__":
    main()
