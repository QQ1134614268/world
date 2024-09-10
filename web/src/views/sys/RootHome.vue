<template>
  <div class="d-flex flex-column flex-grow-1">
    <div class="h1 text-center">科技小栈</div>
    <div class="flex-grow-1 row justify-content-start align-items-center align-content-start">
      <div :key=index v-for="(item, index) in sysUrls " class="m-1" style="width: 10rem;">
        <div class="ratio ratio-1x1">
          <a :href=item.url class="m-1">
            <img src="@/assets/route.webp" alt="加载失败" class="w-100" style="object-fit: fill">
          </a>
        </div>
        <div class="text-center">
          {{ item.name }}
        </div>
      </div>
    </div>
    <div id="footer" class="text-center">
      <div class="w-100">
        <span>备案号：</span>
        <a href="https://beian.miit.gov.cn" target="_blank" class="text-black-50" style="color: #e7e3e3">皖ICP备20002024号-2</a>
      </div>
    </div>
  </div>
</template>

<script>
import {RenrenRootUrl} from "@/views/video";
import {WorkerRootUrl} from "@/views/worker";
import {MemberAdminHome, MemberRootUrl} from "@/views/member";
import {AdminUrl} from "@/views/videoAdmin";
import {HelloRootUrl} from "@/views/hello";
import {TreeRootUrl} from "@/views/tree";
import {USER_LOGIN_URL, USER_REGISTER_URL, UserSpaceRootUrl} from "@/views/user";
import {ENUM_ROOT} from "@/views/sys/index";
import {SystemLevel} from "@/views/level";
import {CodeRootUrl} from "@/views/low_code";

export default {
  name: "RootHome",
  data() {
    return {
      sysUrls: [
        {
          url: CodeRootUrl,
          name: "低代码"
        },
        {
          url: TreeRootUrl,
          name: "真实之树"
        },
        {
          url: SystemLevel,
          name: "等级系统"
        },
        {
          url: RenrenRootUrl,
          name: "人人影"
        },
        {
          url: AdminUrl,
          name: "人人影后台系统"
        },
        {
          url: WorkerRootUrl,
          name: "工时"
        },
        {
          url: MemberRootUrl,
          name: "店铺"
        },
        {
          url: MemberAdminHome,
          name: "店铺后台系统"
        },
        {url: HelloRootUrl, name: "测试"},
        {url: UserSpaceRootUrl, name: "用户空间"},
        {url: USER_REGISTER_URL, name: "注册"},
        {url: USER_LOGIN_URL, name: "登录"},
        {url: ENUM_ROOT, name: "枚举"},
      ],
    }
  }
}
</script>

<style scoped>
</style>
