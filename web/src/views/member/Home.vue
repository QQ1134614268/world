<template>
  <div id="container" class="p_c_box-flex_col p_c_flex_1">
    <div id="header" class="p_c_box-flex_center">
      <div class="p_c_box-flex_center">
        <router-link :to=MemberRootUrl>会员系统</router-link>
      </div>
      <div v-if="user">
        <el-dropdown>
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <a @click="logout">退出登录</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=MemberAdminHome>设置</a>
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div v-else>
        <router-link tag="a" :to=SYS_LOGIN_URL>登陆</router-link>
        |
        <router-link tag="a" :to=SYS_REGISTER_URL>注册</router-link>
      </div>
    </div>
    <box-flex id="body" class="p_c_flex_1">
      <router-view class="p_c_flex_1"/>
    </box-flex>
    <footer class="footer131">

      <div>
        <a :href="MemberRootUrl" class="p_c_HolyGrail-content">
          <BoxCol>
            <!--              <img :src="home_icon">-->
            <img src="@/assets/切图/首页/首页.png" height="35">
            <div>首页</div>
          </BoxCol>
        </a>
      </div>

      <a :href="MemberRootUrl" class="p_c_HolyGrail-content">
        <div>点餐</div>
      </a>
      <a :href="UserSpace" class="p_c_HolyGrail-content">
        <div>购物车</div>
      </a>
      <a :href="UserSpace" class="p_c_HolyGrail-content">
        <div>我的</div>
      </a>
    </footer>
  </div>
</template>
<script>
import {userLogout} from "@/api/user";
import {MemberAdminHome, MemberRootUrl, Store, UserSpace} from "@/views/member/index";
import {SYS_LOGIN_URL, SYS_REGISTER_URL} from "@/views/sys";

export default {
  name: "Home",
  data() {
    return {
      MemberRootUrl,
      Store,
      MemberAdminHome,
      SYS_LOGIN_URL,
      SYS_REGISTER_URL,
      UserSpace,
      menuList: [
        {name: "首页", path: MemberRootUrl},
        {name: "我的", path: UserSpace},
      ],
      store_id: 1,
      // home_icon: require('/assets/img/image1.jpeg')
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
    }
  }
}
</script>
<style scoped>
#container {
  width: 47rem;
  height: 102rem;
}

#header {
  display: flex;
  justify-content: space-around;
}

#body {
  width: 100%;
}

footer {
  display: flex;
  justify-content: space-evenly;
  height: 3rem;
  background: linear-gradient(to top, #f3f3f3, #cccccc, #f3f3f3);
}

footer div {
  flex: 1;
  text-align: center;
  line-height: 3rem;
  color: #555555;
}

.footer131 {
  /*width: 23rem;*/
  height: 5rem;
  background-image: linear-gradient(
      #ffffff,
      #ffffff),
  linear-gradient(
      #ffffff,
      #ffffff);
  background-blend-mode: normal,
  normal;
  box-shadow: 0rem 0rem 0rem 0rem rgba(48, 45, 43, 0.21);
}

footer div:nth-child(n+2) {
  border-left: solid 1px #cccccc;
}


</style>
