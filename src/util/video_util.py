# -*- coding:utf-8 -*-
"""
@Time: 2021/4/12
@Description:
"""

import os

import cv2

from config.conf import DATA_DIR


def get_first_frame_loc(mp4_loc):
    if not isinstance(mp4_loc, str):
        return
    first_frame_loc = mp4_loc.rsplit(".", 1)[0] + ".jpg"  # todo jpg path
    mp4_loc = os.path.join(DATA_DIR, mp4_loc[1:])  # todo
    if not os.path.exists(mp4_loc):
        return
    video_capture = cv2.VideoCapture(mp4_loc)
    success, frame = video_capture.read()
    if success:
        cv2.imwrite(os.path.join(DATA_DIR, first_frame_loc[1:]), frame)
        return first_frame_loc
