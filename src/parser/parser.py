import argparse

from validation.validation import validate_source


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert an image to ASCII art",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--source",
        type=str,
        choices=["camera", "video"],
        default="camera",
        help="Source type: 'camera' for webcam, 'video' for video file",
    )
    # parser.add_argument("-p", "--path", type=str, required=True, help="Path to the image file")

    args = parser.parse_args()
    validate_source(args.source)

    return args
