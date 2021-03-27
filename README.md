# jetson_recording

Scripts for video recording with USB webcam + Jetson Nano / Raspberry Pi. Here, the webcam is assumed to output motion-JPEG encoded frames. 
You can check the image format/resolution of your webcam output by following:

	v4l2-ctl --list-formats-ext

**Note:**
If you are using R32, you need to replace /usr/lib/aarch64-linux-gnu/tegra/libnvjpeg.so with the one at:
[NVIDIA forum link](https://forums.developer.nvidia.com/t/jetpack-4-2-1-nvjpeg-leaking/79812/8)

- rec_H264.sh

  Capture frames from USB webcam and encode in H.264.

- rec_H265.sh

  Capture frames from USB webcam and encode in H.265.

- rec_H265_split.sh

  Capture frames from USB webcam and encode in H.265, split files after specified duration.

  **Note**: most scripts that uses "timeout" are incorrect. "timeout" needs to send SIGINT to gst-launch in order to properly close the output MP4 file.
  
- rec_H265_split.py

  Python version of the H.265 split-recording script. 

- view.sh

  Preview script. Works with the standard Jetson SD card image (even without X-window). 
  **Does not work with [Jetcard](https://github.com/NVIDIA-AI-IOT/jetcard)** (HDMI device not recognized)

## Raspberry pi scripts
- raspi_rec.sh
- raspi_rec.py


## using ffmpeg in OSX

### list devices
	ffmpeg -f avfoundation -list_devices true -i dummy

Output:

	ffmpeg version 4.3.1 Copyright (c) 2000-2020 the FFmpeg developers
	...
	[AVFoundation indev @ 0x7ffcd8704900] AVFoundation video devices:
	[AVFoundation indev @ 0x7ffcd8704900] [0] FaceTime HD Camera (Built-in)
	[AVFoundation indev @ 0x7ffcd8704900] [1] HD webcam-CMS-V43BK
	[AVFoundation indev @ 0x7ffcd8704900] [2] Capture screen 0
	[AVFoundation indev @ 0x7ffcd8704900] AVFoundation audio devices:
	[AVFoundation indev @ 0x7ffcd8704900] [0] USB Microphone
	[AVFoundation indev @ 0x7ffcd8704900] [1] Background Music
	[AVFoundation indev @ 0x7ffcd8704900] [2] MacBook Pro Microphone
	[AVFoundation indev @ 0x7ffcd8704900] [3] Background Music (UI Sounds)
	[AVFoundation indev @ 0x7ffcd8704900] [4] ZoomAudioDevice
	dummy: Input/output error

### preview
Specify the device number listed above. For example, in the above output, the USB webcam "HD webcam-CMS-V43BK" corresponds to device "1"

	ffplay -f avfoundation -video_size 1280x720 -framerate 30 -i 1

### H.264 capture
	ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i 1 -vcodec h264_videotoolbox -b:v 2M test.mp4

### H.265 capture (bitrate)
	ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i 1 -vcodec hevc_videotoolbox -tag:v hvc1 -b:v 5M test2.mp4

### H.265 capture (CRF)
	ffmpeg -f avfoundation -video_size 3840x2160 -framerate 30 -i 1 -vcodec hevc_videotoolbox -tag:v hvc1 -crf 22 test_265.mkv

