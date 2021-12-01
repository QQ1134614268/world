<template>
  <div class="p_c_box_margin target">
    <div class="art_title"><a :href="target_url+'?target_id='+target_id">{{ title }} </a></div>
    <div class="art_body"> {{ content }}</div>
    <AvatarComponent2 :username="username" :user_id="user_id" :avatar="avatar">
    </AvatarComponent2>
  </div>
</template>
<script>
import AvatarComponent2 from "./avatar/AvatarComponent2"

export default {
  name: "TargetComponent",
  components: {AvatarComponent2},
  data() {
    return {
      search: "",
      activeName: "first",
      tableData: [],
      currentPage: 1,
      pageSize: 5,
      totalNum: 0,
      url: "/api/video_api/MarketTargetListApi",
      target_url: "/video/TargetInfo",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      rankData: [],
    }
  },
  props: {
    title: {
      type: String,
      default: ""
    },
    content: {
      type: String,
      default: ""
    },
    username: "",
    user_id: "",
    avatar: "",
    price: "",
    target_id: "",
  }
}
</script>

<style scoped>
.art_title {
  font-size: 2.4rem;
  font-weight: bold;
  color: red;
  margin-bottom: 0.8rem;
  margin-top: 0.8rem;
}

.target {
  margin-top: 0.8rem;
  margin-bottom: 0.8rem;
  padding: 1.6rem;
  border-radius: 1rem;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.art_body {
  margin-bottom: 0.8rem;
  margin-top: 0.8rem;
  font-size: 1.6rem;
}

.art_note {
  font-size: 1rem;
  color: grey;
}
</style>