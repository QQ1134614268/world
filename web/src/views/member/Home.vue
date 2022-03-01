<template>
  <div id="container" class="p_c_box-flex_col">
    <div id="header" class="p_c_box-flex_center">
      <div class="p_c_box-flex_center">
        <router-link :to=MemberRootUrl>会员系统</router-link>
      </div>
      <router-link :to=GoodsList>菜单列表</router-link>
      <div v-if="user">
        <el-dropdown>
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <a @click="logout">退出登录</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=Store>设置</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" :href=Store>店铺</a>
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
    <div id="body">
      <router-view/>
    </div>
    <footer>
      <a :href="MemberRootUrl">点餐</a>
      <a :href="UserSpace">我的</a>
    </footer>
  </div>
</template>
<script>
import {userLogout} from "@/api/user";
import {GoodsList, MemberRootUrl, Store, UserAdmin, UserSpace} from "@/views/member/index";
import {SYS_LOGIN_URL, SYS_REGISTER_URL} from "@/views/sys";

export default {
  name: "Home",
  data() {
    return {
      MemberRootUrl,
      Store,
      SYS_LOGIN_URL,
      SYS_REGISTER_URL,
      GoodsList,
      UserAdmin,
      UserSpace,
      menuList: [
        {name: "首页", path: MemberRootUrl},
        {name: "我的", path: UserSpace},
      ],
      store_id: 1,
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
<style>

#header {
  display: flex;
  justify-content: space-around;
}

#container {
  height: 100vh;
}

#body {
  flex: 1;
  height: 100vh;
  width: 100%;
  overflow-y: scroll;
}

footer {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

</style>
