<template>
  <div class="p_c_box-flex_row-center">
    <div class="col-6">
      <HeaderComponent2 :user_id="user.id" :username="user.username" :avatar="user.avatar" v-if="user">
      </HeaderComponent2>

      <div class="art_title"> {{ target.title }}</div>
      <div class="art_body"> {{ target.content }}</div>
      <div class="art_note"> 佣金:{{ target.price }}</div>
    </div>
  </div>
</template>

<script>
import HeaderComponent2 from "./component/HeaderComponent2"

export default {
  name: "TargetInfo",
  data() {
    return {
      target_id: this.$route.query.target_id,
      search: "",
      activeName: "first",
      target: {},
      url: "/api/video_api/TargetApi",
      user_url: "/api/video_api/VideoUserApi",
      file_url2: process.env.VUE_APP_BASE_URL + "/api/file/FileApi2?path=",
      user: "",
    }
  },
  components: {HeaderComponent2},
  methods: {
    async init() {

      let result = await this.$get2(this.url, this.target_id)
      if (result.data.code == 1) {
        this.target = result.data.data
        document.title = this.target.title
      } else {
        this.$message('失败');
      }
      let result2 = await this.$get2(this.user_url, this.target.user_id)
      if (result.data.code == 1) {
        this.user = result2.data.data
      } else {
        this.$message('失败');
      }
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>
.art_title {
  font-size: 2.4rem;
  font-weight: bold;
  color: blue;
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
  margin-bottom: 0.8rem;
  margin-top: 0.8rem;
  color: #72727f;
  font-size: 1.6rem;
}
</style>