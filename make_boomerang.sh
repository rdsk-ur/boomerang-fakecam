#!/bin/sh
input=$1
output=output.mp4

ffmpeg -y -i $input -filter_complex "[0]reverse[r];[0][r]concat=n=2" -r 15 $output
