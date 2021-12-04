<template>
  <div class="p_c_box-flex_row-center">
    <!--        <el-avatar :src="file_url2+avatar" fit="contain"-->
    <!--                   :class="{width:width,height:height}">-->
    <!--        </el-avatar>-->
    <el-avatar :src="file_url2+avatar" fit="contain" :style="{width: width,height: height}"></el-avatar>
    <span>
            {{ username }}
        </span>
  </div>
</template>

<script>

export default {
  name: "AvatarComment",
  data() {
    return {
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
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