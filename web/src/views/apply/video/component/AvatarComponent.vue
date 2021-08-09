<template>
  <AvatarComponentBase
      :username="username"
      :user_id="user_id"
      :avatar="avatar"
      :user_url="user_url"
      :create_time="create_time"
  >
  </AvatarComponentBase>
</template>

<script>
import AvatarComponentBase from "@/views/apply/video/component/AvatarComponentBase";

export default {
  name: "AvatarComment",
  data() {
    return {
      user_url: "/video/UserInfo"
    }
  },
  components: {AvatarComponentBase},
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
    }
  }
}
</script>

<style scoped>

</style>