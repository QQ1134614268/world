<template>
  <div class="p_c_HolyGrail-body">
    <div class="p_c_box-flex_row-center " style="height: 3rem">
      <div style="flex: 1" class="p_c_box-flex_row-center title2">工时系统</div>
      <div class="p_c_flexbox_row" style="width: 12rem">
        <WorkerUserIcon></WorkerUserIcon>
      </div>
    </div>
    <div class="p_c_flexbox_row">
      <div class="col-2">
        <el-menu router :default-active="this.$route.fullPath" active-text-color="#409EFF">
          <el-menu-item :index="item.menuPath" v-for="(item, index) in menuList" :key="index">
            <template slot="title">
              <i :class="item.menuIcon"></i>
              <span>
                {{ item.menuName }}
              </span>
            </template>
          </el-menu-item>
        </el-menu>
      </div>
      <div class="col-10">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import WorkerUserIcon from "@/components/WorkerUserIcon";
import {
  workConfig,
  worker,
  workLog,
  workTimeAnalyse,
  workTimeInfo,
  workTimeRecord,
  workTimeReport
} from "@/views/worker/index";

export default {
  name: 'HomeComponent',
  data() {
    return {
      data: [],
      menuList: [
        {
          menuName: "考勤打卡",
          menuPath: workTimeRecord,
          menuIcon: "el-icon-connection",
        },
        {
          menuName: "考勤信息",
          menuPath: workTimeInfo,
          menuIcon: "el-icon-info",
        },
        {
          menuName: "工人列表",
          menuPath: worker,
          menuIcon: "el-icon-location ",
        },
        {
          menuName: "报表看板",
          menuPath: workTimeAnalyse,
          menuIcon: "el-icon-data-analysis",
        },
        {
          menuName: "统计看板",
          menuPath: workTimeReport,
          menuIcon: "el-icon-data-analysis",
        },
        {
          menuName: "配置",
          menuPath: workConfig,
          menuIcon: "el-icon-setting",
        },
        {
          menuName: "操作日志",
          menuPath: workLog,
          menuIcon: "el-icon-document",
        }
      ]
    };
  },

  components: {
    WorkerUserIcon
  },
  methods: {}
}
</script>
<style>
.title2 {
    font-size: 2rem;
    color: black;
}

</style>