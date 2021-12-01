<template>
  <div class="p_c_box_margin p_c_box-shadow" >
    <ThumbnailComponent :describe="describe" :thumbnail="thumbnail" :id="id">
    </ThumbnailComponent>
    <AvatarComponent :username="username" :user_id="user_id" :avatar="avatar" :create_time="create_time">
    </AvatarComponent>
  </div>
</template>

<script>
import AvatarComponent from "./avatar/AvatarComponent"
import ThumbnailComponent from "./ThumbnailComponent"

export default {
  name: "VideoCard",
  data() {
    return {
      video_url: "/video/Video",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
    }
  },
  components: {
    AvatarComponent,
    ThumbnailComponent
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
    thumbnail: {
      type: String,
      default: ""
    },
    describe: {
      type: String,
      default: ""
    },
    id: {
      type: Number,
      default: ""
    },
  }
}
</script>

<style scoped>

</style>