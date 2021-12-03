<template>
  <div class="p_c_flexbox">
    <div>
      <el-menu default-active="1" active-text-color="#409EFF">
        <el-menu-item index="1">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span slot="title">
              <router-link to="worker" class="p_c_space">
                工人列表
              </router-link>
            </span>
          </template>
        </el-menu-item>
        <el-menu-item index="2">
          <template slot="title">
            <i class="el-icon-setting"></i>
            <span slot="title">
              <router-link to="workTimeRecord" class="p_c_space">
                考勤打卡
              </router-link>
            </span>
          </template>
        </el-menu-item>
        <el-menu-item index="3">
          <template slot="title">
            <i class="el-icon-info"></i>
            <span slot="title">
              <router-link to="time" class="p_c_space">
                考勤信息
              </router-link>
            </span>
          </template>
        </el-menu-item>
        <el-menu-item index="4">
          <template slot="title">
            <i class="el-icon-data-analysis"></i>
            <span slot="title">
              <router-link to="workTimeAnalyse" class="p_c_space">
                统计看板
              </router-link>
            </span>
          </template>
        </el-menu-item>
      </el-menu>

    </div>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data() {
    return {
    };
  },
  methods: {
  }
}
</script>
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>