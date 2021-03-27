#!/bin/sh
OUTFILE=test.mp4
WIDTH=1280
HEIGHT=720

gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! \
	       image/jpeg,framerate=30/1,width=${WIDTH},height=${HEIGHT} ! \
	       nvjpegdec ! \
	       video/x-raw ! \
	       nvvidconv ! \
	       nvv4l2h264enc ! \
	       h264parse ! \
	       qtmux ! \
	       filesink location=${OUTFILE} \
	       -e
