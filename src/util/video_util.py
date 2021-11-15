# -*- coding:utf-8 -*-
"""
@Time: 2021/4/12
@Description:
"""

import os
import threading

import cv2

from config.conf import DATA_DIR
from util.log_util import logger


def get_first_frame_loc(mp4_loc):
    if not isinstance(mp4_loc, str):
        return
    first_frame_loc = mp4_loc.rsplit(".", 1)[0] + ".jpg"

    mp4_loc = os.path.join(DATA_DIR, mp4_loc)
    if not os.path.exists(mp4_loc):
        return
    video_capture = cv2.VideoCapture(mp4_loc)
    success, frame = video_capture.read()
    if success:
        cv2.imwrite(os.path.join(DATA_DIR, first_frame_loc), frame)
        return first_frame_loc


class mp4_to_H264():
    def __init__(self):
        pass

    def convert_avi(self, input_file, output_file, ffmpeg_exec="ffmpeg"):
        ffmpeg = '{ffmpeg} -y -i "{infile}" -c:v libx264 -strict -2 "{outfile}"'.format(
            ffmpeg=ffmpeg_exec,
            infile=input_file,
            outfile=output_file)
        # subprocess.call(ffmpeg)
        os.system(ffmpeg)

    def convert_avi_to_webm(self, input_file, output_file, ffmpeg_exec="ffmpeg"):
        return self.convert_avi(input_file, output_file, ffmpeg_exec="ffmpeg")

    def convert_avi_to_mp4(self, input_file, output_file, ffmpeg_exec="ffmpeg"):
        return self.convert_avi(input_file, output_file, ffmpeg_exec="ffmpeg")

    def convert_to_avcmp4(self, input_file, output_file, ffmpeg_exec="ffmpeg"):
        email = threading.Thread(target=self.convert_avi, args=(input_file, output_file, ffmpeg_exec,))
        email.start()

    def convert_byfile(self, from_path, to_path):
        if not os.path.exists(from_path):
            print("Sorry, you must create the directory for the output files first")
        if not os.path.exists(os.path.dirname(to_path)):
            os.makedirs(os.path.dirname(to_path), exist_ok=True)
        directory, file_name = os.path.split(from_path)
        raw_name, extension = os.path.splitext(file_name)
        print("Converting ", from_path)
        self.convert_avi_to_mp4(from_path, to_path)


def deal_video(src_path):
    file = src_path
    # 判断文件夹是否存在
    if os.path.exists(file):
        pass
    else:
        # 文件不存在退出
        logger.warning("file not exit:", file)
        return
    if file.endswith(".mp4") or file.endswith(".MP4"):
        try:
            p, f = os.path.split(file)
            newP = os.path.join(p, "videoId" + f)
            # 使用mediainfo工具获取视频编码格式
            from pymediainfo import MediaInfo
            mi = MediaInfo.parse(file)
            print(mi)
            myFormat = mi.to_data()['tracks'][1]['format']

            if myFormat != "AVC":
                logger.info(file, myFormat)
                # 处理视频cmd命令
                fftool = "ffmpeg.exe"
                cmd = fftool + " -i " + file + " -vcodec h264 -threads 5 -preset ultrafast " + newP
                cmd = cmd.replace("\\", "/")
                os.system(cmd)
            else:
                print("not deal", myFormat)
        except IOError:
            logger.error("处理失败:", file)


if __name__ == '__main__':
    a = mp4_to_H264()
    from_path = r'D:\桌面文件夹\movie.mp4'
    to_path = 'D:\桌面文件夹\movie.h264.mp4'
    a.convert_byfile(from_path, to_path)
