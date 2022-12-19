<template>
  <div class="member_container">
    <div class="member_header">
      <div @click="goTo(MemberRootUrl)" class="title">
        会员系统
      </div>
      <el-dropdown v-if="user">
        <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>
            <div @click="logout">退出登录</div>
          </el-dropdown-item>
          <el-dropdown-item>
            <div @click="goTo(MemberAdminHome)">设置</div>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <div v-else>
        <span @click="goTo(SYS_LOGIN_URL)"> 登陆</span>
        <span> | </span>
        <span @click="goTo(SYS_REGISTER_URL)"> 登陆</span>
      </div>
    </div>
    <div class="member_body">
      <router-view/>
    </div>
    <div class="member_footer">
      <div @click="goTo(MemberRootUrl)">
        <div style="height: 24px">
          <img src="@/assets/切图/首页/首页.png">
        </div>
        <div>首页</div>
      </div>
      <div @click="goTo(UserSpace)">
        <div style="height: 24px">
          <img src="@/assets/切图/首页/首页.png">
        </div>
        <div>点餐</div>
      </div>
      <div @click="goTo(UserSpace)">
        <div style="height: 24px">
          <img src="@/assets/切图/首页/首页.png">
          <!--          <img src="@/assets/切图/首页/首页.png" style="height: 24px">-->
        </div>
        <!--        <img src="@/assets/切图/首页/首页.png" style="height: 24px">-->
        <div>我的</div>
      </div>
    </div>
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
    },
    goTo(url) {
      this.$router.push(url)
    }
  }
}
</script>
<style scoped lang="less">
.member_container {
  height: 100vh;
  display: flex;
  flex-direction: column;

  @media only screen and (min-width: 768px) {
    width: 678px;
  }
  @media only screen and (max-width: 768px) {
    width: 100%;
  }
}

div {
  //border: 1px solid red;
}

.member_header {
  display: flex;
  flex: 0 0 1;
  justify-content: space-around;
  height: 48px;
}

.member_body {
  width: 100%;
  display: flex;
  flex-grow: 1;
}

.member_footer {
  display: flex;
  justify-content: space-evenly;
  height: 3rem;
  background: linear-gradient(to top, #f3f3f3, #cccccc, #f3f3f3);

  div {
    border: black 1px solid;
  }
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
  background-image: linear-gradient(#ffffff, #ffffff), linear-gradient(#ffffff, #ffffff);
  background-blend-mode: normal, normal;
  box-shadow: 0rem 0rem 0rem 0rem rgba(48, 45, 43, 0.21);
}

footer div:nth-child(n+2) {
  border-left: solid 1px #cccccc;
}


</style>
