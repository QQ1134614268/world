# -*- coding:utf-8 -*-
"""
@Time: 2021/4/12
@Description:
"""
import os

import cv2

import util.unique_util
from config.conf import JPG
from config.env_default import world_env


def get_first_frame_loc(video_path):
    if not os.path.exists(video_path):
        return
    file_name = util.unique_util.get_uuid() + JPG
    save_path = os.path.join(world_env.upload_file_path2, file_name)
    video_capture = cv2.VideoCapture(video_path)
    success, frame = video_capture.read()
    if success:
        cv2.imwrite(save_path, frame)
        return world_env.upload_file_dir_name + file_name
