<template>
  <div class="p_c_HolyGrail-body">
    <div id="header" class="p_c_box-flex_center">
      <div class="p_c_box-flex_center">
        <a href="/">
          <img src="@/assets/icon/favicon2.jpg" style="width: 4rem; border-radius: 45rem">
        </a>人人影
      </div>
      <router-link tag="a" to="/video/Market"> 达人</router-link>
      <router-link tag="a" to="/video/Market2"> 赞助商</router-link>

      <div v-if="user">
        <el-dropdown>
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <a @click="logout">退出登录</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href="'/video/video_user?user_id='+user.id">用户空间</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=WorksUrl>我的作品</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" href="/video/Target">我的发布</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" href="/video/InvitationCode" v-if="INVITATION_CODE">我的邀请码</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" href="/videoAdmin" v-if="VIDEO_REVIEW">审核</a>
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
        <a href="http://www.beian.miit.gov.cn" target="_blank" style="color: #e7e3e3">皖ICP备20002024号-1</a>
      </div>
    </div>
  </div>
</template>
<script>
import jwt_decode from 'jwt-decode';
import {hasPermission, userLogout} from "@/api/user";
import {VideoLoginUrl, VideoRegisterUrl, WorksUrl} from "@/api/routerUrl";
import {Permission} from "@/api/config";

export default {
  name: "App",
  data() {
    return {
      VideoLoginUrl,
      VideoRegisterUrl,
      WorksUrl,
      INVITATION_CODE: false,
      VIDEO_REVIEW:false
    }
  },
  computed: {
    user() {
      // 这里存储从store里获取的token的数据
      if (this.$store.state.token) {
        let user = jwt_decode(this.$store.state.token)
        return user
      }
    }
  },
  methods: {
    logout() {
      userLogout(this)
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
