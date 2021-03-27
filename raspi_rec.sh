#!/bin/sh

# unset auto-focus
v4l2-ctl -c focus_auto=0 -c focus_absolute=0

timeout 5m gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! omxh264enc target-bitrate=6000000 control-rate=variable ! video/x-h264,profile=high ! h264parse ! mpegtsmux ! filesink location=test.ts -e

