<template>
  <div class="p_c_HolyGrail-body">
    <div id="header" class="p_c_box-flex_center">
      <div class="p_c_box-flex_center">
        <a href="/">
          <img src="@/assets/icon/favicon2.jpg" style="width: 2.5rem; border-radius: 28rem">
        </a>人人影
      </div>
      <router-link tag="a" :to=VIDEO_MARKET> 达人</router-link>
      <router-link tag="a" :to=VIDEO_MARKET2> 赞助商</router-link>

      <div v-if="user">
        <el-dropdown>
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <a @click="logout">退出登录</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href="video_user+'?user_id='+user.id">用户空间</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=WorksUrl>我的作品</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=Target>我的发布</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=InvitationCode v-if="INVITATION_CODE">我的邀请码</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=AdminUrl v-if="VIDEO_REVIEW">审核</a>
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div v-else>
        <router-link tag="a" :to=VideoLoginUrl> 登陆</router-link>
        |
        <router-link tag="a" :to=VideoRegisterUrl> 注册</router-link>
      </div>
    </div>

    <div id="body" class="p_c_HolyGrail-body">
      <router-view/>
    </div>
    <div id="footer">
      <div>
        客服微信: i17601083308
      </div>
      <div>
        <span>备案号：</span>
        <a href="https://beian.miit.gov.cn" target="_blank" style="color: #e7e3e3">皖ICP备20002024号-1</a>
      </div>
    </div>
  </div>
</template>
<script>
import {hasPermission, userLogout} from "@/api/user";
import {Permission} from "@/api/config";
import {
  InvitationCode,
  Target,
  VIDEO_MARKET,
  VIDEO_MARKET2,
  video_user,
  VideoLoginUrl,
  VideoRegisterUrl,
  WorksUrl
} from "@/views/video/index";
import {AdminUrl} from "@/views/videoAdmin";

export default {
  name: "App",
  data() {
    return {
      Target,
      AdminUrl,
      InvitationCode,
      video_user,
      VIDEO_MARKET2,
      VIDEO_MARKET,
      VideoLoginUrl,
      VideoRegisterUrl,
      WorksUrl,
      INVITATION_CODE: false,
      VIDEO_REVIEW: false
    }
  },
  computed: {
    user() {
      return this.$store.state.userInfo
    }
  },
  methods: {
    async logout() {
      await userLogout()
      this.$message.info("退出登陆")
    },
    async init() {
      if (this.user && this.user.id) {
        this.INVITATION_CODE = await hasPermission(this.user.id, Permission.INVITATION_CODE)
      }
      if (this.user && this.user.id) {
        this.VIDEO_REVIEW = await hasPermission(this.user.id, Permission.VIDEO_REVIEW)
      }
    }
  },
  created() {
    this.init()
  }
}
</script>
<style>

#header {
  display: flex;
  justify-content: space-around;
  height: 10%;
}

#footer {
  text-align: center;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 1;
  }
  50.01% {
    opacity: 0;
  }
  /* 注意这里定义50.01%立刻透明度为０，可以设置闪烁效果 */
  100% {
    opacity: 0;
  }
}

.blink {
  animation: blink .75s linear infinite;
  /* 其它浏览器兼容性前缀 */
  -webkit-animation: blink .75s linear infinite;
  -moz-animation: blink .75s linear infinite;
  -ms-animation: blink .75s linear infinite;
  -o-animation: blink .75s linear infinite;
  color: #dd4814;
}
</style>
