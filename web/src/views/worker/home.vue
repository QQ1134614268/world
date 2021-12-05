<template>
  <div>
    <div class="p_c_box-flex_row-center " style="height: 10rem">
      <div class="title2">工时系统</div>
    </div>
    <div class="p_c_flexbox_row">
      <div class="col-2">
        <el-menu default-active="1" active-text-color="#409EFF">
          <router-link to="workTimeInfo">
            <el-menu-item index="1">
              <template slot="title">
                <i class="el-icon-info"></i>
                <span slot="title">
                    考勤信息
                </span>
              </template>
            </el-menu-item>
          </router-link>
          <router-link to="workTimeRecord">
            <el-menu-item index="2">
              <template slot="title">
                <i class="el-icon-setting"></i>
                <span slot="title">
                    考勤打卡
                </span>
              </template>
            </el-menu-item>
          </router-link>
          <router-link to="worker">
            <el-menu-item index="3">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span slot="title">
                    工人列表
                </span>
              </template>
            </el-menu-item>
          </router-link>
          <router-link to="workTimeAnalyse">
            <el-menu-item index="4">
              <template slot="title">
                <i class="el-icon-data-analysis"></i>
                <span slot="title">
                  统计看板
                </span>
              </template>
            </el-menu-item>
          </router-link>
          <router-link to="config">
            <el-menu-item index="5">
              <template slot="title">
                <i class="el-icon-connection"></i>
                <span slot="title">
                  配置
                </span>
              </template>
            </el-menu-item>
          </router-link>
          <router-link to="log">
            <el-menu-item index="6">
              <template slot="title">
                <i class="el-icon-document"></i>
                <span slot="title">
                  操作日志
                </span>
              </template>
            </el-menu-item>
          </router-link>
        </el-menu>
      </div>
      <div class="col-10">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data() {
    return {
      data: []
    };
  },
  methods: {}
}
</script>
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>