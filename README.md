# Loop Fake Webcam

Feed a fake webcam based on a looped video file and pretend that you are paying attention to whatever online conversation you have.

Note that this is currently for Linux only.

## Requirements

Python packages:

+ open cv
+ pyfakewebcam

For creating virtual webcam (linux only):

    sudo apt install v4l2loopback-utils

## Usage

Create the virtual webcam (linux only):

``` sh
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback devices=1 video_nr=20 card_label="v4l2loopback" exclusive_caps=1
```

You most likely want to use a boomerang-style video for your fake loop. To build on, you can use `make_boomerang.sh`:

    ./make_boomerang.sh fake_source.mp4

This will create `output.mp4` which you can use for the loop script.

Now you can start the `loop.py` script to feed the virtual camera with your video:

    python3 loop.py /path/to/videofile

You may use any video file type that OpenCV supports.
