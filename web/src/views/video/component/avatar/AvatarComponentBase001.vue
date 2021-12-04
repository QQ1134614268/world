<template>
  <div class="p_c_box-flex_row-center">
    <el-avatar :src="file_url2+avatar" fit="contain" :class="{width:width,height:height}"></el-avatar>
    <span> {{ username }} </span>
  </div>
</template>

<script>

export default {
  name: "AvatarCommentBase",
  data() {
    return {
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }
  },
  props: {
    avatar: {
      type: String,
      default: ""
    },
    username: {
      type: String,
      default: ""
    },
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