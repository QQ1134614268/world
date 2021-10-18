<template>
  <div class="box">
    <AvatarComponentBase0
        :username="username"
        :user_id="user_id"
        :avatar="avatar"
        :user_url="user_url"
    ></AvatarComponentBase0>
  </div>
</template>

<script>
import AvatarComponentBase0 from "./AvatarComponentBase0"

export default {
  name: "AvatarCommentBase",
  components: {AvatarComponentBase0},
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
    user_id: {
      type: Number,
      default: ""
    },
    create_time: {
      type: String,
      default: ""
    },
    user_url: {
      type: String,
      default: ""
    }
  }
}
</script>

<style scoped>
.box {
  display: flex;
  justify-content: space-between;
}
</style>