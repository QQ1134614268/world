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
    <div>
      <a @click="logOut">
        <div style="width: 10rem">
          <img src="@/assets/route.webp">
        </div>
        <div>退出登录</div>
      </a>
    </div>
  </div>
</template>

<script>

import {
  AdminUrl,
  HelloRootUrl,
  MemberRootUrl,
  messageRootUrl,
  RegisterRootUrl,
  RenrenRootUrl,
  SYS_LOGIN_URL,
  TreeRootUrl,
  UserSpaceRootUrl,
  WorkerRootUrl
} from "@/api/routerUrl";
import {userLogout} from "@/api/user";

export default {
  name: "root",
  data() {
    return {
      sysUrls: [
        {url: TreeRootUrl, name: "真实之树"},
        {url: RenrenRootUrl, name: "人人影"},
        {url: WorkerRootUrl, name: "工时"},
        {url: MemberRootUrl, name: "店铺"},
        {url: AdminUrl, name: "后台系统"},
        {url: HelloRootUrl, name: "测试"},
        {url: messageRootUrl, name: "消息"},
        {url: UserSpaceRootUrl, name: "用户空间"},
        {url: RegisterRootUrl, name: "注册"},
        {url: SYS_LOGIN_URL, name: "登录"},
      ],
    }
  },
  methods: {
    logOut() {
      userLogout(this)
      this.$message("退出")
    }
  }
}
</script>

<style scoped>

</style>
