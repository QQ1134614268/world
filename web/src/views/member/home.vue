<template>
  <div id="container" class="p_c_box-flex_col">
    <div id="header" class="p_c_box-flex_center">
      <div class="p_c_box-flex_center">
        <router-link to="/member">会员系统</router-link>
      </div>
      <router-link :to=GoodsList> 菜单列表</router-link>
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
    <footer class="p_c_box-flex">
      <div>
        首页
      </div>
      <div>
        活动
      </div>
      <div>
        点餐
      </div>
      <div>
        消息
      </div>
      <div>
        我的
      </div>
    </footer>
  </div>
</template>
<script>
import jwt_decode from 'jwt-decode';
import {userLogout} from "@/api/user";
import {SYS_LOGIN_URL, SYS_REGISTER_URL} from "@/api/routerUrl";
import {GoodsList} from "@/views/member/index";

export default {
  name: "home",
  data() {
    return {
      SYS_LOGIN_URL,
      SYS_REGISTER_URL,
      GoodsList
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
