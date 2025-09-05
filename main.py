from PIL import Image


def load_img(path):
    img = Image.open(path)

    return img


def resize_img(img, target_width=300):
    w, h = img.size
    aspect_ratio = h / w

    new_height = int(target_width * aspect_ratio)
    resized_img = img.resize((target_width, new_height))

    return resized_img


def to_grayscale(img):
    gray_img = img.convert("L")

    return gray_img

def map_brightness(img):
    ascii_chars = '@%#*+=-:. '

    pixels = img.getdata()
    w, _ = img.size

    row_idx = 0
    ascii_img = ''

    for pixel in pixels:
        if row_idx <= w:
            ascii_chars_idx = pixel * (len(ascii_chars) - 1) // 255
            ascii_char = ascii_chars[ascii_chars_idx] 

            ascii_img = ascii_img + ascii_char 

            row_idx += 1
        else:
            ascii_img = ascii_img + '\n'
            row_idx = 0

    return ascii_img


def main():
    try:
        img = load_img("/mnt/c/Users/dgafo/Downloads/pug.jpg")
    except Exception:
        print("Failed to load Image")
        return

    print(img.format)


if __name__ == "__main__":
    main()
