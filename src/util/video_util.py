# -*- coding:utf-8 -*-
"""
@Time: 2021/4/12
@Description:
"""

import os

import cv2

import util.unique_util
from config.conf import JPG
from config.dir_conf import UPLOAD_FILE_PATH2, UPLOAD_FILE_DIR_NAME


def get_first_frame_loc(video_path):
    if not os.path.exists(video_path):
        return
    file_name = util.unique_util.get_uuid() + JPG
    save_path = os.path.join(UPLOAD_FILE_PATH2, file_name)
    video_capture = cv2.VideoCapture(video_path)
    success, frame = video_capture.read()
    if success:
        cv2.imwrite(save_path, frame)
        return UPLOAD_FILE_DIR_NAME + file_name
