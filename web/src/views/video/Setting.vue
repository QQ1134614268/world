<template>
  <div>
    <el-form ref="form" :model="form" label-width="8rem" :rules="rules" style="padding: 1rem">
      <el-form-item label="头像">
        <WrdVueCropper :url="form.avatar" @getUrl="getUrl"></WrdVueCropper>
      </el-form-item>
      <el-form-item label="手机号" prop="phone" :required="true">
        <el-input v-model="form.phone" style="width: 10rem"></el-input>
      </el-form-item>
      <el-form-item label="签名">
        <el-input v-model="form.describe" style="width: 10rem"></el-input>
      </el-form-item>
      <el-form-item label="微信号">
        <el-input v-model="form.wechat_number" style="width: 10rem"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="save">保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {FileApi, UserApi} from "@/api/api";
import {updateUser} from "@/api/user";
import {getUserIdByToken} from "@/api/util";
import WrdVueCropper from "@/components/WrdVueCropper";
import {get2} from "@/api/http";

export default {
  name: "video_user",
  components: { WrdVueCropper},
  data() {
    return {
      form: {},
      FileApi,
      rules: {
        phone: [{required: true, message: '手机号不能为空', trigger: 'blur'}],
      },
    }
  },
  methods: {
    async init() {
      let user_id = getUserIdByToken()
      let result = await get2(UserApi, user_id, {})
      if (result.data.code == 1) {
        this.form = result.data.data
      } else {
        this.$message.error('操作失败');
      }
    },
    getUrl(url) {
      this.form.avatar = url
    },
    async save() {
      await updateUser(this.form)
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