#!/usr/bin/python3
import os
import sys
import time
import gi

# recording time in sec
rec_time = 60 * 5
outfile = "test.ts"

# unset auto-focus
print("unsetting auto-focus")
os.system('v4l2-ctl -c focus_auto=0 -c focus_absolute=0')

gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(sys.argv)

# Logitech 
str_pipeline = "v4l2src device=/dev/video0 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! omxh264enc target-bitrate=6000000 control-rate=variable ! video/x-h264,profile=high ! h264parse ! mpegtsmux ! filesink location=%s" % outfile
pipeline = Gst.parse_launch (str_pipeline)
bus = pipeline.get_bus()

print("Starting pipeline")
pipeline.set_state(Gst.State.PLAYING)

time.sleep(rec_time)

print("Stopping pipeline")
pipeline.send_event(Gst.Event.new_eos())
print("Waiting for the EOS message on the bus")
bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.EOS)
pipeline.set_state(Gst.State.NULL) 
