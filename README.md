# Boomerang Fake Webcam

Feed a fake webcam based on a video file.

The video is played boomerang-style: the video is infinitely played forward and then backwards as long as the script is running.

Note that this is currently for Linux only.

## Requirements

Python packages:

+ moviepy
+ pyfakewebcam

Install opencv for performance improvements (e.g. `apt-get install python-opencv` on Ubuntu).

For creating virtual webcam (linux only):

    sudo apt install v4l2loopback-utils

## Usage

Create the virtual webcam (linux only):

``` sh
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=20 card_label="v4l2loopback" exclusive_caps=1
```

Now you can start the `boomerang.py` script to feed the virtual camera with a boomerang version of the provided video:

    python3 boomerang.py /path/to/videofile

You may use any video file type that `moviepy` supports.
