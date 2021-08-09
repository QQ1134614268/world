<template>
  <div class="hello" style="line-height:4rem;">
    <div v-for="item in routes">
      <a :href=item>{{ item }}</a>
    </div>
    <div v-for="item in sysUrls ">
      <a :href=item.url>{{ item.name }}</a>
    </div>
  </div>
</template>

<script>

export default {
  name: "root",
  data() {
    return {
      routes: [
        "/hello",
        "/worker",
      ],
      sysUrls: [
        {url: "/diary/diary_list", name: "日志列表"},
        {url: "/diary/add_diary", name: "写日志"},
        {url: "/message/message", name: "消息"},
        {url: "/model/object", name: "真实之树"},
        {url: "/apply/music/Music", name: "音乐"},
        {url: "/member/Store", name: "店铺"},
        {url: "/user/UserSpace", name: "用户空间"},
        {url: "/sys/register", name: "注册"},
        {url: "/sys/login", name: "登录"},
        {url: "/worker2/Person", name: "工时2/人员"},
        {url: "/worker2/Time", name: "工时2/时间"},
      ],
    }
  }
}
</script>

<style scoped>

</style>
