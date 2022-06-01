<template>
  <div>
    <el-upload :action="FileApi" :on-success="handleSuccess" class="avatar-uploader">
      <video v-if="url" :src="url" class="avatar"></video>
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      <div class="el-upload__tip" slot="tip">请上传视频，且不超过 10MB</div>
    </el-upload>
    <div>上传结果: {{ url }}</div>
  </div>
</template>
<script>
import {FileApi} from "@/api/api";

// const vConsole =new VConsole()

export default {
  data() {
    return {
      FileApi,
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      url: ""
    };
  },
  methods: {
    handleSuccess(res, file) {
      this.url = URL.createObjectURL(file.raw);
    },
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