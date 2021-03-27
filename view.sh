#!/bin/bash
gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! \
	       image/jpeg,framerate=30/1,width=1280,height=720 ! \
	       jpegparse ! \
	       nvjpegdec ! \
	       video/x-raw ! \
	       nvvidconv ! \
	       nvoverlaysink
