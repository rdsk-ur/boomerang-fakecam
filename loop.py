from argparse import ArgumentParser
import cv2
import pyfakewebcam
import time

def main(video_file, device):
    cap = cv2.VideoCapture(video_file)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print("FPS:", cap.get(cv2.CAP_PROP_FPS))
    sleep_duration = 1 / cap.get(cv2.CAP_PROP_FPS)

    fake = pyfakewebcam.FakeWebcam(device, width, height)
    print("ready")
    while cap.isOpened():
        time.sleep(sleep_duration)
        ret, frame = cap.read()
        if ret:
            fake.schedule_frame(frame[...,::-1])
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    cap.release()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("video", help="Can be anything that moviepy can handle.")
    parser.add_argument("--device", default="/dev/video20", help="The path to the virtual webcam, created using v4l2loopback")
    args = parser.parse_args()

    try:
        main(args.video, args.device)
    except KeyboardInterrupt:
        print("\rAborted")
