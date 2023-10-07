<template>
  <div>
    <el-upload
        action="#"
        accept=IMG_TYPE_STR
        :auto-upload="false"
        :show-file-list="false"
        :on-change='changeUpload'
        :before-upload='beforeUpload'
    >
      <el-image v-if="url" :src="url" style="width: 150px;height: 150px"></el-image>
      <i v-if="!url" class="el-icon-upload"></i>
      <div v-if="!url" class="el-upload__text">点击上传</div>
    </el-upload>
    <el-dialog title="图片剪裁" :visible.sync="dialogVisible" append-to-body>
      <div class="cropper-content">
        <div class="cropper" style="text-align:center">
          <VueCropper
              ref="cropper"
              :img="option.img"
              :outputType="option.outputType"
              :info="option.info"
              :canScale="option.canScale"
              :autoCrop="option.autoCrop"
              :fixed="option.fixed"
              :canMove="option.canMove"
              :canMoveBox="option.canMoveBox"
              :centerBox="option.centerBox"
          >
          </VueCropper>
        </div>
      </div>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="finish">确认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {FileApi} from "@/api/api";
import {beforeImgUpload} from "@/api/util";
import {IMG_TYPE_STR} from "@/api/config";
import {postForm} from "@/api/http";

export default {
  props: {
    url: String
  },
  data() {
    return {
      option: { //参考网址 https://github.com/xyxiao001/vue-cropper
        img: "", // 裁剪图片的地址 , url地址, base64, blob
        outputType: "jpeg",
        info: true,
        canScale: true,
        autoCrop: true,
        fixed: true,
        canMove: false,
        canMoveBox: true,
        // original:true //上传图片按照原始比例渲染
        centerBox: true
      },
      dialogVisible: false,
      IMG_TYPE_STR,
      FileApi,
    }
  },
  methods: {
    beforeUpload(file) {
      return beforeImgUpload(file)
    },
    // 上传按钮   限制图片大小
    changeUpload(file, fileList) {
      let url = URL.createObjectURL(file.raw)
      this.$nextTick(() => {
        this.option.img = url;
        // this.option.img = file.url
        this.dialogVisible = true
      })
    },
    async finish() {
      let formData = new FormData();
      this.$refs.cropper.getCropBlob(async (data) => {
        formData.append("file", data, "cropper.png");
        let result = await postForm(FileApi, formData)
        if (result.data.code == 1) {
          this.dialogVisible = false
          // this.url = result.data.data
          this.$emit("getUrl", result.data.data)
        } else {
          this.$message.error("上传失败!")
        }
      })
    }
  }
}
</script>
<style lang="less">
// 截图
.cropper-content {
  .cropper {
    width: auto;
    height: 300px;
  }
}
</style>