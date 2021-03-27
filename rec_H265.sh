#!/bin/sh
gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! \
	       image/jpeg,framerate=30/1,width=3840,height=2160 ! \
	       nvjpegdec ! \
	       video/x-raw ! \
	       nvvidconv ! \
	       nvv4l2h265enc bitrate=15000000 ! \
	       h265parse ! \
	       splitmuxsink max-size-time=1800000000000 location=test4K_%04d.mp4 \
	       -e
