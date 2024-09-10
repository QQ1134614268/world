<template>
  <div>
    <el-upload
        class="avatar-uploader"
        :action="FileApi"
        :accept="accept"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :on-progress="handleProgress"
        :before-upload="beforeAvatarUpload">
      <video v-if="fileUrl" :src="fileUrl" class="avatar"></video>
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      <div class="el-upload__tip" slot="tip">请上传视频，且不超过 10MB</div>
    </el-upload>
    <el-progress class="progressModule" :percentage="Number(uploadPercentage)" v-if="showProgress "></el-progress>
  </div>
</template>
<script>
import {FileApi} from "@/api/api";
import {videoBeforeUpload} from "@/api/util";
import {VIDEO_TYPE_STR} from "@/api/config";

export default {
  name: "WrdVideoUploadV2",
  // props: {
  //   fileUrl: {
  //     type: String,
  //   },
  // },
  data() {
    return {
      showProgress: false,
      uploadPercentage: "",
      FileApi,
      accept: VIDEO_TYPE_STR,
      fileUrl: ""
    };
  },
  methods: {
    handleProgress(res, file, fileList) {
      this.showProgress = true
      this.uploadPercentage = file.percentage.toFixed(0)
    },
    handleAvatarSuccess(res, file) {
      this.showProgress = false
      if (res.code !== 1) {
        this.$message.error(res.data)
        return
      }
      this.fileUrl = URL.createObjectURL(file.raw);
      this.$message.success("上传成功")
      this.$emit("getUrl", res.data)
    },
    beforeAvatarUpload(file) {
      return videoBeforeUpload(file)
    }
  }
}
</script>
<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 6rem;
  height: 6rem;
  line-height: 3rem;
  text-align: center;
}

.avatar {
  width: 6rem;
  height: 6rem;
  display: block;
}
</style>
