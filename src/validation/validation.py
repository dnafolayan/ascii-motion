import os
import sys


def validate_path(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist")
        sys.exit(1)

    if not os.path.isfile(path):
        print(f"Path '{path}' is not a file")
        sys.exit(1)

    if not path.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
        print(f"File '{path}' is not a supported video format")
        sys.exit(1)


def validate_source(source):
    if source not in ["camera", "video"]:
        print(f"Source '{source}' is not supported. Choose 'camera' or 'video'.")
        sys.exit(1)
