import os
import time
from pymediainfo import MediaInfo
import logging

# ffmpeg.exe path 需要写绝对路径，或者把ffmpeg.exe文件放到同级py文件
fftool = "ffmpeg.exe"

def dealVideo(srcPath):
    file  = srcPath
    # 判断文件夹是否存在
    if os.path.exists(file):
        pass
    else:
        # 文件不存在退出
        logging.warning("file not exit:",file)
        return
    if file.endswith(".mp4") or file.endswith(".MP4"):
        try:
            p, f = os.path.split(file)
            newP = os.path.join(p, videoId + f)
            # 使用mediainfo工具获取视频编码格式
            mi = MediaInfo.parse(file)
            myFormat = mi.to_data()['tracks'][1]['format']

            if myFormat != "AVC":
                logging.info(file, myFormat)
                # 处理视频cmd命令
                cmd = fftool + " -i " + file + " -vcodec h264 -threads 5 -preset ultrafast " + newP
                cmd = cmd.replace("\\","/")
                os.system(cmd)
            else:
                print("not deal",myFormat)
        except IOError:
            logging.error("处理失败:",file)

if __name__ == '__main__':
    global addVideoList
    global videoId
    videoId = "temporary-h264-"
    addVideoList = []

    # star 用于记录当前处理到第几个视频文件
    star = 0
    while True:
        # 打开保存有视频路径的txt
        with open("video.txt", mode="r") as f:
            count = 0
            for line in f.readlines():
                line = line.strip('\n')
                if count == star:
                    dealVideo(line)
                    # 处理了一个视频，指针加一
                    star+=1
                count += 1
