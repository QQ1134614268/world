<template>
  <div>
    <el-upload
        id="audioUpload"
        class="avatar-uploader"
        :action="FileApi"
        :show-file-list="true"
        :multiple="false"
        :file-list="fileList"
        :limit="1"
        :auto-upload="true"
        :on-change="handleChangeAudio"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload">
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <div slot="tip" class="el-upload__tip" style="margin-bottom: 10px">
        只能上传mp3文件，且不超过2M，播放长度不超过60s
      </div>
    </el-upload>
  </div>
</template>
<script>

import {FileApi} from "@/api/api";

export default {

  name: 'hello',
  data() {
    return {
      message: 'default',
      msg2: 'first',
      FileApi,
      fileList: [],
      audioDuration: undefined
    }
  },
  methods: {
    handleChangeAudio() {
      console.log("handleChangeAudio")
    },
    handleAvatarSuccess() {
      console.log("handleChangeAudio")
    },
    beforeAvatarUpload(file) {
      // 文件类型进行判断
      const isAudio = true
      // 限制上传文件大小 2M
      debugger
      const isLt2M = file.size / 1024 / 1024 < 2;
      const isTime60S = this.audioDuration >= 60 ? true : '';
      // 获取时长
      this.getTimes(file);
      if (!isAudio) {
        this.$message.error("上传文件只能是Mp3格式!");
        this.fileList = [];
      } else {
        if (!isLt2M) {
          this.$message.error("上传文件大小不能超过 2MB!");
          this.fileList = [];
        } else {
          if (!isTime60S) {
            this.$message.error("上传文件时长不能超过60秒!");
            this.fileList = [];
          }
        }
      }
      return isAudio && isLt2M && isTime60S
    },
    getTimes(file) {
      let content = file;
      //获取录音时长
      let url = URL.createObjectURL(content);
      //经测试，发现audio也可获取视频的时长
      let audioElement = new Audio(url);
      let duration;
      audioElement.onloadedmetadata = () => {
        duration = audioElement.duration; //时长为秒，取整
      };
      return duration
    },
  }
}
</script>
