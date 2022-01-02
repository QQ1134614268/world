<template>
  <div class="p_c_box-flex_center">
    <el-avatar :src="imgUrl"></el-avatar>
    <span> {{ username }} </span>
  </div>
</template>

<script>
export default {
  name: "UserAvatarIComponent",
  data() {
    return {
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }
  },
  props: {
    imgUrl: {
      type: String,
      default: ""
    },
    username: {
      type: String,
      default: ""
    },
  }
}
</script>

<style scoped>

</style>