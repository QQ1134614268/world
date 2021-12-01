<template>
  <div>
    <div v-if="this.form.role">
      <span>邀请码--</span>
      <span>{{ code }}</span>
      <el-button @click="updateCode" v-if="code"> 更新</el-button>
      <el-button @click="createCode" v-else> 生成</el-button>
    </div>
    <el-form ref="form" :model="form" label-width="8rem" :rules="rules" style="padding: 1rem">
      <el-form-item label="头像">
        <el-upload style="width: 10%;height: 10%" drag :auto-upload="false" :show-file-list="false"
                   :on-change='changeUpload'>
          <img v-if="form.avatar" :src="file_url+'?path='+form.avatar" class="avatar">
          <div v-else>
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">点击上传</div>
            <div class="el-upload__tip">支持绝大多数图片格式，单张图片最大支持5MB</div>
          </div>
        </el-upload>
      </el-form-item>
      <el-form-item label="手机号" prop="phone" :required="true">
        <el-input v-model="form.phone" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item label="签名">
        <el-input v-model="form.describe" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item label="身份证">
        <el-input v-model="form.id_card" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item label="执照">
        <el-upload style="width: 10%;height: 10%"
                   :show-file-list="false"
                   :action="file_url"
                   :on-success="uploadLicense">
          <img v-if="form.business_license" :src="file_url+'?path='+form.business_license">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="商标">
        <el-upload style="width: 10%;height: 10%"
                   :show-file-list="false"
                   class="upload-demo"
                   :action="file_url"
                   :on-success="uploadBrand"
        >
          <img v-if="form.brand" :src="file_url+'?path='+form.brand" class="avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i></el-upload>
      </el-form-item>
      <el-form-item label="简历">
        <el-upload style="width: 10%;height: 10%"
                   :show-file-list="false"
                   class="upload-demo"
                   :action="file_url"
                   :on-success="uploadResume"
        >
          <img v-if="form.resume" :src="file_url+'?path='+form.resume" class="avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="微信号">
        <el-input v-model="form.wechat_number" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item label="抖音号">
        <el-input v-model="form.tiktok_number" style="width: 16rem"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="save">保存</el-button>
      </el-form-item>
    </el-form>
    <el-dialog title="图片剪裁" :visible.sync="dialogVisible" append-to-body>
      <div class="cropper-content">
        <div class="cropper p_c_test_border" style="text-align:center">
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
              :fixedBox="option.fixedBox"
          ></VueCropper>
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

import jwt_decode from "jwt-decode";

export default {
  name: "video_user",
  data() {
    return {
      user_id: this.$route.query.user_id,
      file_url: process.env.VUE_APP_BASE_URL + '/api/file/FileApi2',
      form: {},
      url: "/api/video_api/VideoUserApi",
      url2: "/api/video_api/InvitationCodeApi",
      rules: {
        phone: [{required: true, message: '手机号不能为空', trigger: 'blur'}],
      },
      code: "",
      user_role: "",
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
    // 上传按钮   限制图片大小
    changeUpload(file, fileList) {
      let url = URL.createObjectURL(file.raw)

      const isLt5M = file.size / 1024 / 1024 < 5
      if (!isLt5M) {
        this.$message.error('上传文件大小不能超过 5MB!')
        return false
      }
      this.fileinfo = file
      // 上传成功后将图片地址赋值给裁剪框显示图片
      this.$nextTick(() => {
        console.log(file)
        this.option.img = url;
        // this.option.img = file.url
        this.dialogVisible = true
      })
    },
    // 点击裁剪，这一步是可以拿到处理后的地址
    async finish() {
      let file_url = process.env.VUE_APP_BASE_URL + '/api/file/FileApi2'
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
    handleChange(file, fileList) {
      this.fileList = fileList.slice(-3);
    },
    uploadAvatar(res, file, fileList) {
      this.form.avatar = res.data
    },
    uploadLicense(res, file, fileList) {
      this.form.business_license = res.data
    },
    uploadBrand(res, file, fileList) {
      this.form.brand = res.data
    },
    uploadResume(res, file, fileList) {
      this.form.resume = res.data
    },
    async init() {
      let user = jwt_decode(localStorage.getItem("token"))
      let result = await this.$get2(this.url, this.user_id)
      if (result.data.code == 1) {
        this.form = result.data.data
      } else {
        this.$message('');
      }
    },
    async init2() {
      let result = await this.$get2(this.url2, this.user_id)
      if (result.data.code == 1) {
        this.code = result.data.data.code
      } else {
        this.$message('');
      }
    },
    async updateCode() {
      let result = await this.$putJson2(this.url2, 0)
      if (result.data.code == 1) {
        await this.init2()
      } else {
        this.$message('');
      }
    },
    async createCode() {
      let result = await this.$postJson2(this.url2, 0)
      if (result.data.code == 1) {
        await this.init2()
      } else {
        this.$message('');
      }
    },
    async save() {
      let result = await this.$putJson2(this.url, this.form.id, this.form)
      if (result.data.code == 1) {
        this.$message('修改成功!');
      } else {
        this.$message('');
      }
    },
  },
  created() {
    this.init()
    this.init2()
  }
}
</script>

<style scoped>
.cropper {
  width: auto;
  height: 300px;
}
</style>