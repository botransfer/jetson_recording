#!/usr/bin/python3
import gi
import sys
import time
import datetime

# recording time in seconds
#rec_time = 60 * 60 * 5
rec_time = 60 * 30

# 10Mbps
bitrate = 15000 * 1000

# split size
split_time = 60 * 30 * 1000000000

# need to add timestamp 
str_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
out_template = "%s_%%03d.mp4" % (str_now)

gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(sys.argv)

str_p  = "v4l2src device=/dev/video0 io-mode=2 ! "
str_p += "image/jpeg,framerate=30/1,width=1920,height=1080 ! "
str_p += "nvjpegdec ! "
str_p += "video/x-raw ! nvvidconv ! "
str_p += "nvv4l2h265enc bitrate=%d ! " % bitrate
str_p += "h265parse ! "
str_p += "splitmuxsink max-size-time=%d location=%s" % (split_time, out_template)

pipeline = Gst.parse_launch (str_p)
bus = pipeline.get_bus()

pipeline.set_state(Gst.State.PLAYING)

try:
    time.sleep(rec_time)
except KeyboardInterrupt:
    print("ctrl-c pressed")

pipeline.send_event(Gst.Event.new_eos())
print("Waiting for the EOS message on the bus")
bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.EOS)
print("Stopping pipeline")
pipeline.set_state(Gst.State.NULL) 
