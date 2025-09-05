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

# map brightness to ascii chars

def main():
    try:
        img = load_img("/mnt/c/Users/dgafo/Downloads/pug.jpg")
    except Exception:
        print("Failed to load Image")
        return

    print(img.format)


if __name__ == "__main__":
    main()
