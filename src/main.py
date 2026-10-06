import os
import time
from parser.parser import parse_args, request_video_path

import cv2

from image_transformation.image_transformation import frame_to_ascii


def play_vid(args):
    try:
        if args.source == "video":
            cap = cv2.VideoCapture(request_video_path())  # for video file input
        else:
            cap = cv2.VideoCapture(0)  # for camera input

        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_duration = 1 / fps
        next_frame_time = time.perf_counter()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if args.source == "camera":
                frame = cv2.flip(frame, 1)  # for camera input

            ascii_frame = frame_to_ascii(frame)
            os.system("cls" if os.name == "nt" else "clear")
            print(ascii_frame)

            next_frame_time += frame_duration
            sleep_time = next_frame_time - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                next_frame_time = time.perf_counter()
    except KeyboardInterrupt:
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("Video playback interrupted.")
    finally:
        cap.release()


def main():
    args = parse_args()
    play_vid(args)


if __name__ == "__main__":
    main()
