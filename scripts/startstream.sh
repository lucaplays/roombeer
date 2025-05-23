#!/bin/bash
# Thanks to https://github.com/jacksonliam/mjpg-streamer
./mjpg_streamer/mjpg_streamer -i "./mjpg_streamer/input_uvc.so -d /dev/video0 -r 1280x720 -f 10" -o "./mjpg_streamer/output_http.so -p 1234 -w ./www"
