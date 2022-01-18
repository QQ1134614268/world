<template>
  <div class="p_c_HolyGrail-body">
    <div id="header" class="p_c_box-flex_center">
      <div class="p_c_box-flex_center">
        <router-link to="/member">会员系统</router-link>
      </div>
      <div v-if="user">
        <el-dropdown>
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <a @click="logout">退出登录</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" href="/member/Store">设置</a>
            </el-dropdown-item>
            <el-dropdown-item>
              <a type="primary" href="/member/Store">店铺</a>
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div v-else>
        <router-link tag="a" :to=SYS_LOGIN_URL> 登陆</router-link>
        |
        <router-link tag="a" :to=SYS_REGISTER_URL> 注册</router-link>
      </div>
    </div>
    <div id="body">
      <router-view/>
    </div>
  </div>
</template>
<script>
import jwt_decode from 'jwt-decode';
import {userLogout} from "@/api/user";
import {SYS_LOGIN_URL, SYS_REGISTER_URL} from "@/api/routerUrl";

export default {
  name: "home",
  data() {
    return {
      SYS_LOGIN_URL,
      SYS_REGISTER_URL
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
    }
  }
}
</script>
<style>

#header {
  display: flex;
  justify-content: space-around;
}


</style>
