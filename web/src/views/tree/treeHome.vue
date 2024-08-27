<template>
  <div class="p_c_HolyGrail-body">
    <BoxRow class="header">
      <div class="title">真实之树</div>
      <div class="avtar">
        <div v-if="user">
          <el-dropdown @command="handleCommand">
        <span class="el-dropdown-link">
          <el-avatar :src="user.avatar" :key="user.avatar"></el-avatar>
        </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
        <div v-else>
          <el-button @click="login">登录</el-button>
          <el-button @click="register">注册</el-button>
        </div>
      </div>
    </BoxRow>
    <div class="p_c_HolyGrail-body">
      <router-view/>
      <!--      <router-view  name="tree"/>-->
    </div>
    <div id="footer" class="p_c_box-flex_row-center">
      <a href="https://beian.miit.gov.cn" target="_blank" style="color: #e7e3e3">皖ICP备20002024号-2</a>
    </div>
  </div>
</template>

<script>
import {userLogout} from "@/api/user";

export default {
  name: "treeHome",
  methods: {
    async logout() {
      await userLogout()
    },
    handleCommand(command) {
      this.$message('click on item ' + command);
    }
  },
  computed: {
    user() {
      return this.$store.state.userInfo
    }
  },
}
</script>
<style scoped>

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title {
  text-align: center;
  flex: 1;
  font-weight: bold;
}

.avtar {
  width: 10rem;
}

#footer {
  text-align: center;
}

</style>
