#!/bin/bash

libcamera-vid --width 640 --height 480 --bitrate 2048000 -n -t 0 -o /dev/stdout | ffmpeg -i - -vcodec mpeg4 -b:v 2M -acodec aac -f mpegts - | cefputstream ccnx:/stream -r 2 -b 1400 -t 3600 -e 3600
