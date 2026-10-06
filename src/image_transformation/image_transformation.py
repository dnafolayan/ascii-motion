import cv2
from PIL import Image


def resize_frame(img, target_width=160):
    w, h = img.size
    aspect_ratio = h / w

    new_height = int(target_width * aspect_ratio * 0.55)
    resized_frame = img.resize((target_width, new_height), Image.Resampling.LANCZOS)

    return resized_frame


def to_grayscale(frame):
    gray_frame = frame.convert("L")

    return gray_frame


def map_brightness(frame):
    ascii_chars = " .:-=+*#%@"
    # ascii_chars = ascii_chars[::-1]

    pixels = frame.getdata()
    w, _ = frame.size

    row_idx = 0
    ascii_str = ""

    for pixel in pixels:
        ascii_chars_idx = pixel * (len(ascii_chars) - 1) // 255
        ascii_char = ascii_chars[ascii_chars_idx]

        ascii_str = ascii_str + ascii_char

        row_idx += 1

        if row_idx == w:
            ascii_str = ascii_str + "\n"
            row_idx = 0

    return ascii_str


def frame_to_ascii(frame, width=160):
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    img = to_grayscale(resize_frame(img, target_width=width))

    ascii_str = map_brightness(img)
    return ascii_str
