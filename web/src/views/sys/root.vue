<template>
  <div class="rootPage">
    <h1 style="text-align: center">科技小栈</h1>
    <div class="body">
      <div :key=index v-for="(item, index) in sysUrls " class="imgItem">
        <div class="imgBox">
          <div class="parent">
            <a :href=item.url>
              <img src="@/assets/route.webp" class="child img1" alt="加载失败">
            </a>
          </div>
          <div class="desc">
            {{ item.name }}
          </div>
        </div>
      </div>
    </div>
    <div id="footer">
      <div>
        <span>备案号：</span>
        <a href="https://beian.miit.gov.cn" target="_blank" style="color: #e7e3e3">皖ICP备20002024号-2</a>
      </div>
    </div>
  </div>
</template>

<script>
import {RenrenRootUrl} from "@/views/video";
import {WorkerRootUrl} from "@/views/worker";
import {MemberRootUrl} from "@/views/member";
import {AdminUrl} from "@/views/videoAdmin";
import {HelloRootUrl} from "@/views/hello";
import {TreeRootUrl} from "@/views/tree";
import {USER_LOGIN_URL, USER_REGISTER_URL, UserSpaceRootUrl} from "@/views/user";
import {ENUM_ROOT} from "@/views/sys/index";
import {SystemLevel} from "@/views/level";
import {CodeRootUrl} from "@/views/low_code";

export default {
  name: "root",
  data() {
    return {
      sysUrls: [
        {url: CodeRootUrl, name: "低代码"},
        {url: TreeRootUrl, name: "真实之树"},
        {url: SystemLevel, name: "等级系统"},
        {url: RenrenRootUrl, name: "人人影"},
        {url: WorkerRootUrl, name: "工时"},
        {url: MemberRootUrl, name: "店铺"},
        {url: AdminUrl, name: "后台系统"},
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
#footer {
  text-align: center;
}

.rootPage {
  display: flex;
  flex-direction: column;

  .body {
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    flex-grow: 1;

    .imgItem {
      width: 10rem;
      padding: 1rem;


      .imgBox {
        width: 100%;

        .img1 {
          object-fit: fill;
        }

        .desc {
          display: flex;
          justify-content: center;
        }
      }
    }
  }
}

.parent {
  position: relative;
  width: 100%;
  padding-bottom: 100%;
}

.child {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}


</style>
