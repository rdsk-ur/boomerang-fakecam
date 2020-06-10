#!/usr/bin/env python3
from argparse import ArgumentParser
import time
from moviepy.video.io.VideoFileClip import VideoFileClip
import pyfakewebcam

def main(video_file: str, device: str):
    clip = VideoFileClip(video_file)
    fake = pyfakewebcam.FakeWebcam(device, clip.w, clip.h)

    print("webcam ready on", device)

    ref_time = time.time()

    while True:
        rel_time = time.time() - ref_time
        if rel_time > 2 * clip.duration:
            rel_time -= 2 * clip.duration
            ref_time += 2 * clip.duration

        try:
            frame = clip.get_frame(abs(rel_time - clip.duration))
            fake.schedule_frame(frame)
        except OSError:
            # there is an error with get_frame on the first/last frame
            print("skip")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("video", help="Can be anything that moviepy can handle.")
    parser.add_argument("--device", default="/dev/video20", help="The path to the virtual webcam, created using v4l2loopback")
    args = parser.parse_args()

    try:
        main(args.video, args.device)
    except KeyboardInterrupt:
        print("\rAborted")
