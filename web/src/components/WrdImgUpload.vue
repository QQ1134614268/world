<template>
  <el-upload
      class="avatar-uploader"
      :action="FileApi"
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload">
    <img v-if="fileUrl" :src="fileUrl" class="avatar">
    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    <div class="el-upload__tip" slot="tip">请上传图片，且不超过5MB</div>
  </el-upload>
</template>
<script>
import {FileApi} from "@/api/api";
import {beforeImgUpload} from "@/api/util";

export default {
  name: "WrdImgUpload",
  props: {
    fileUrl: {
      type: String,
    },
  },
  data() {
    return {
      FileApi,
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      if (res.code !== 1) {
        this.$message.error(res.data)
        return
      }
      this.$message.success("上传成功")
      this.$emit("getUrl", res.data)
    },
    beforeAvatarUpload(file) {
      return beforeImgUpload(file)
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
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}

.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
