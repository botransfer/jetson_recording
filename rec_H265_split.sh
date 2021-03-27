#!/bin/sh

TOTAL_DUR=1m
SPLIT_SEC=15
SPLIT_NANO=$((${SPLIT_SEC} * 1000000000))
BITRATE=$((4 * 1000 * 1000))
WIDTH=1920
HEIGHT=1080

# unset auto-focus
# v4l2-ctl -c focus_auto=0 -c focus_absolute=0

# stop in 5 hours
timeout --foreground --signal=INT ${TOTAL_DUR} \
gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! \
	image/jpeg,framerate=30/1,width=${WIDTH},height=${HEIGHT} ! \
	nvjpegdec ! \
	video/x-raw ! nvvidconv ! \
	nvv4l2h265enc bitrate=${BITRATE} ! \
	h265parse ! \
	splitmuxsink muxer=qtmux max-size-time=${SPLIT_NANO} location=test%02d.mp4 \
	-e
