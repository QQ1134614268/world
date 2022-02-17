<template>
  <div>
    <el-form ref="form" :model="form" label-width="8rem" :rules="rules" style="padding: 1rem">
      <el-form-item label="头像">
        <el-upload style="width: 10%;height: 10%" :show-file-list="false" :action="FileApi" :key="form.avatar"
                   :on-success="uploadAvatar">
          <img v-if="form.avatar" :src="form.avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon">点击上传</i>
        </el-upload>
      </el-form-item>
      <el-form-item label="手机号" prop="phone" :required="true">
        <el-input v-model="form.phone" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item label="签名">
        <el-input v-model="form.describe" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item label="微信号">
        <el-input v-model="form.wechat_number" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="save">保存</el-button>
      </el-form-item>
    </el-form>
    <el-dialog title="图片剪裁" :visible.sync="dialogVisible" append-to-body>
      <div class="cropper-content">
        <div class="cropper p_c_test_border" style="text-align:center">
          <!--          todo func finish, VueCropper参数-->
          <VueCropper
              ref="cropper"
              :img="option.img"
              :outputSize="option.size"
              :outputType="option.outputType"
              :info="true"
              :full="option.full"
              :canMove="option.canMove"
              :canMoveBox="option.canMoveBox"
              :original="option.original"
              :autoCrop="option.autoCrop"
              :autoCropWidth="option.autoCropWidth"
              :autoCropHeight="option.autoCropHeight"
              :fixedBox="option.fixedBox">
          </VueCropper>
        </div>
      </div>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="finish" :loading="loading">确认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>

import {FileApi, UserApi} from "@/api/api";
import {getUserIdByToken, updateTokenAndInfo} from "@/api/user";

export default {
  name: "video_user",
  data() {
    return {
      user_id: getUserIdByToken(),
      form: {},
      FileApi: FileApi,
      rules: {
        phone: [{required: true, message: '手机号不能为空', trigger: 'blur'}],
      },
      dialogVisible: false,
      // 裁剪组件的基础配置option
      option: {
        img: '', // 裁剪图片的地址
        autoCropWidth: 150,
        autoCropHeight: 150,
        canMove: true,
        canMoveBox: true, // 截图框能否拖动
        info: true, // 裁剪框的大小信息
        canScale: false, // 图片是否允许滚轮缩放
        autoCrop: true, // 是否默认生成截图框

        fixedBox: true, // 固定截图框大小 不允许改变
        // fixed: true, // 是否开启截图框宽高固定比例
        // fixedNumber: [7, 5], // 截图框的宽高比例
        full: false, // 是否输出原图比例的截图

        original: false, // 上传图片按照原始比例渲染
        // centerBox: false, // 截图框是否被限制在图片里面
        // infoTrue: true, // true 为展示真实输出图片宽高 false 展示看到的截图框宽高,
        outputType: 'png', // 裁剪生成图片的格式
        outputSize: 1, // 裁剪生成图片的质量
      },
      loading: false
    }
  },

  methods: {
    async finish() {
      // todo 优化 抽方法
      let file_url = process.env.VUE_APP_BASE_URL + FileApi
      let formData = new FormData();
      this.$refs.cropper.getCropBlob(async (data) => {
        let img = window.URL.createObjectURL(data)
        this.model = true;
        this.modelSrc = img;
        formData.append("file", data, "cropper.png");
        let result = await this.$postForm(file_url, formData)
        if (result.data.code) {
          this.dialogVisible = false
          this.form.avatar = result.data.data
        } else {
          this.$message("失败!")
        }
      })
    },
    uploadAvatar(res, file, fileList) {
      this.form.avatar = res.data
    },
    async init() {
      let result = await this.$get2(UserApi, this.user_id)
      if (result.data.code == 1) {
        this.form = result.data.data
      } else {
        this.$message('');
      }
    },
    async save() {
      let result = await this.$putJson2(UserApi, this.form.id, this.form)
      await updateTokenAndInfo()
      if (result.data.code == 1) {
        this.$message('修改成功!');
      } else {
        this.$message('');
      }
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
.cropper {
  width: auto;
  height: 300px;
}
</style>