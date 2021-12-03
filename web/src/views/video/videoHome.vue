<template>
  <div style="min-height: 100%">
    <div id="header" class="p_c_box-flex_center ">
      <div style="" class="p_c_box-flex_center ">
        <a href="/">
          <img src="@/assets/icon/favicon2.jpg" style="width: 4rem; border-radius: 45rem">
        </a>人人影
      </div>
      <!--       <a href="/sys/root">root</a>-->
      <!--      <a href="/message/message">消息</a>-->
      <a type="primary" href="/video/Market" class="">达人</a>
      <a type="primary" href="/video/Market2">赞助商</a>
      <div v-if="user.id">
        <el-dropdown>
          <span class="el-dropdown-link">
            <AvatarPureComponent :user_id="user.id" style="display: inline" v-if="user.id"></AvatarPureComponent>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <a @click="logout">退出登录</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href="'/video/video_user?user_id='+user.id">用户空间</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" href="/video/works">我的作品</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" href="/video/Target">我的发布</a>
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div v-else>
        <!--        <a href="/sys/login">登陆</a>&#45;&#45;-->
        <a href="/video/login">登陆</a> |
        <a href="/video/register">注册</a>
      </div>
    </div>

    <div id="body">
      <!--        搜索-->
      <!--        设置-->
      <!--                <div> 侧边导航栏</div>-->
      <!--# 仿 pycharm风格  另设置一处,查找一处-->
      <!--# 左侧 root的分类叉树,新增 删除-->
      <!--# 中上 select查找 其下分类查找-->
      <!--# 中间改变-->
      <!--# 右侧消息列表,类似弹幕-->
      <!--# 最下输出-->
      <router-view/>
    </div>
    <div id="footer">
      <div>
        <a href="http://www.6liuzhibo.com/public/index.php/mobile/common/video/player_sharing/0/power_id/0/store_id/184/with_id/3872/type/3/invite_id/15521439.html">
          <div style="height: 5rem">
<!--            <img src="@/assets/advert.jpg" style="height:100%" class="blink">-->
          </div>
        </a>
      </div>
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
import HeaderComponent from '@/views/video/component/avatar/HeaderComponent'
import AvatarPureComponent from '@/views/video/component/avatar/AvatarPureComponent'

export default {
  name: "App",
  components: {HeaderComponent, AvatarPureComponent},
  data() {
    return {}
  },
  computed: {
    user() {
      // 这里存储从store里获取的token的数据 todo
      if (this.$store.state.token) {
        return jwt_decode(this.$store.state.token)
      }
      return {}
    }
  },
  methods: {
    logout() {
      localStorage.removeItem("token")
      this.$store.commit('receiveUserInfo', {
        token: ""
      })
    }
  }
}
</script>
<style>

#header {
  display: flex;
  justify-content: space-around;
  height: 10%;
}

#body {
  min-height: 80%
}

#footer {
  text-align: center;
  height: 10%;
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
