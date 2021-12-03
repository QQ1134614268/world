<template>
  <div class="p_c_flexbox">
    <div v-for="item in sysUrls ">
      <a :href=item.url>
        <div class="p_c_box-flex_col-center">
          <div style="width: 10rem">
            <img src="@/assets/route.webp">
          </div>
          <div>{{ item.name }}</div>
        </div>
      </a>
    </div>
  </div>
</template>

<script>

export default {
  name: "root",
  data() {
    return {
      sysUrls: [
        {url: "/tree", name: "真实之树"},
        {url: "/video", name: "人人影"},
        {url: "/worker", name: "工时"},
        {url: "/member/Store", name: "店铺"},
        {url: "/hello", name: "测试"},
        {url: "/diary/diary_list", name: "日志列表"},
        {url: "/diary/add_diary", name: "写日志"},
        {url: "/message/message", name: "消息"},
        {url: "/apply/music/Music", name: "音乐"},
        {url: "/user/UserSpace", name: "用户空间"},
        {url: "/sys/register", name: "注册"},
        {url: "/sys/login", name: "登录"},
      ],
    }
  }
}
</script>

<style scoped>

</style>
