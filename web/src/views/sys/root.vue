<template>
  <div class="p_c_flexbox">
    <div v-for="item in sysUrls ">
      <a :href=item.url>
        <div class="p_c_box-flex_col-center">
          <div style="width: 8rem">
            <img src="@/assets/route.webp">
          </div>
          <div>{{ item.name }}</div>
        </div>
      </a>
    </div>
    <div>
      <a @click="logOut">
        <div style="width: 6rem">
          <img src="@/assets/route.webp">
        </div>
        <div>退出登录</div>
      </a>
    </div>
  </div>
</template>

<script>

import {userLogout} from "@/api/user";
import {RenrenRootUrl} from "@/views/video";
import {WorkerRootUrl} from "@/views/worker";
import {MemberRootUrl} from "@/views/member";
import {messageRootUrl} from "@/views/message";
import {AdminUrl} from "@/views/videoAdmin";
import {HelloRootUrl} from "@/views/hello";
import {TreeRootUrl} from "@/views/tree";
import {UserSpaceRootUrl} from "@/views/user";
import {RegisterRootUrl, SYS_LOGIN_URL} from "@/views/sys/index";

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
    async logOut() {
      await userLogout()
      this.$message("退出")
    }
  }
}
</script>

<style scoped>

</style>
