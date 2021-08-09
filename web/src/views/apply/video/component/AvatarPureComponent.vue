<template>
  <div :class="{width:width,height:height}">
    <el-avatar :src="file_url2+user.avatar" fit="contain" v-if="user.avatar" alt="123"></el-avatar>
    <el-avatar src="@/assets/avatar.png" alt="123" v-else></el-avatar>
  </div>
</template>

<script>
export default {
  name: "AvatarCommentBase",
  data() {
    return {
      url2: '/api/video_api/VideoUserApi',
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      user: {},
    }
  },
  methods: {
    async init() {
      let result = await this.$get2(this.url2, this.user_id, {})
      if (result.data.code == 1) {
        this.user = result.data.data
      } else {
        this.$message('失败');
      }
    },
  },
  created() {
    this.init()
  },
  props: {
    user_id: "",
    width: {
      type: String,
      default: "1.5rem"
    },
    height: {
      type: String,
      default: "1.5rem"
    }
  }
}
</script>

<style scoped>

</style>