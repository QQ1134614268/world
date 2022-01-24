<template>
  <div style="display:flex; align-items:center ; flex-direction: column; ">
    <div>
      <router-link to="Setting">编辑</router-link>
    </div>
    <el-avatar :src="form.avatar" :key="form.avatar"></el-avatar>
    <div> 签名: {{ form.describe }}</div>
    <div> 手机号: {{ form.phone }}</div>
    <div> 微信号: {{ form.wechat_number }}</div>

  </div>
</template>

<script>
import {FileApi, UserApi} from "@/api/api";

export default {
  name: "video_user",
  data() {
    return {
      user_id: this.$route.query.user_id,
      form: {},
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
      let formData = new FormData();
      this.$refs.cropper.getCropBlob(async (data) => {
        let img = window.URL.createObjectURL(data)
        this.model = true;
        this.modelSrc = img;
        formData.append("file", data, "cropper.png");
        let result = await this.$postForm(FileApi, formData)
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
      let result = await this.$get2(UserApi, this.user_id)
      if (result.data.code == 1) {
        this.form = result.data.data
      } else {
        this.$message('');
      }
    },
    async save() {
      let result = await this.$putJson2(UserApi, this.form.id, this.form)
      if (result.data.code == 1) {
        this.$message('修改成功!');
      } else {
        this.$message('');
      }
    },
    async edit() {

    }
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