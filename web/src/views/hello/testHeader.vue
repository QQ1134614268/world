<template>
  <div>
    <div class="p_c_flexbox_row p_c_test_border p_c_box-flex_center" style="height: 6rem">
      <div style="flex: 1" class="p_c_box-flex_row-center">真实之树</div>
      <div class="p_c_flexbox_row p_c_test_border" style="width: 20rem" v-if="1">
        <el-dropdown @command="handleCommand">
          <!--            <span class="el-dropdown-link">-->
          <el-avatar :src="imgUrl"></el-avatar>
          <!--              <i class="el-icon-arrow-down el-icon&#45;&#45;right"></i>-->
          <!--            </span>-->
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="a">退出登录</el-dropdown-item>
            <el-dropdown-item command="a">设置</el-dropdown-item>
            <el-dropdown-item command="a">用户空间</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div v-else>
        <el-button @click="login">登录</el-button>
        <el-button @click="login">注册</el-button>
        <!--    todo 需要刷新 使用vuex 等 ,溢出改变同步全局-->
      </div>
    </div>
    <div id="body">
      333
      <router-view/>
      <!--      <router-view  name="tree"/>-->
    </div>
    <div id="footer" class="p_c_box-flex_row-center">
      <a href="http://www.beian.miit.gov.cn" target="_blank" style="color: #e7e3e3">皖ICP备20002024号-1</a>
    </div>
  </div>
</template>

<script>

import UserIconCMPO from "@/components/UserIconCMPO";

export default {
  name: "test",
  data() {
    return {
      imgUrl: "http://127.0.0.1:9090/api/file/FileApi2?path=upload_file/963e329ab7f411eb849580fa5b6c6ed4_movie.jpg",
    }
  },
  components: {
    UserIconCMPO
  },
  methods: {
    handleCommand() {
    }
  }
}
</script>

<style scoped>
img, video {
  object-fit: contain;
  max-width: none;
  height: auto;
}

img.a {
  width: 200px;
  height: 400px;
  object-fit: cover;
}
</style>
