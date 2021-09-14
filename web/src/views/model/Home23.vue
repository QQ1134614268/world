<template>
  <el-menu
      :router="true"
      :default-active="(this.$route.meta[0].meta&&this.$route.meta[0].meta[0].path&&!this.$route.meta[0].meta[0].ispath)?this.$route.meta[0].meta[0].path:this.$route.meta[0].path"
      active-text-color="#ffffff"
      :unique-opened="true"
      background-color="#00bfb8"
  >
    <menutree :data="navigation" class="hr_one"></menutree>
    <!-- 侧边导航组件 -->
  </el-menu>

</template>
<script>
export default {
  data() {
    return {
      navigation: [
        {
          id: 0,
          name: "首页",
          path: "/Hr-index/home",
          icon: "icon_hrIndex.png"
        },
        {
          id: 1,
          name: "教职工档案",
          path: "/Hr-index/staffFiles",
          icon: "icon_staffFiles.png"
        },
        {
          id: 2,
          name: "招聘信息",
          path: "",
          icon: "icon_hrJion.png",
          children: [
            {id: 122, name: "招聘申请", path: "/Hr-index/zpApply"},
            {id: 123, name: "招聘审核", path: "/Hr-index/zpCheck"},
            {id: 124, name: "结果统计", path: "/Hr-index/resultInfo"}
          ]
        },
        {
          id: 10,
          name: "解聘信息",
          path: "",
          icon: "icon_hrunBind.png",
          children: [
            {id: 119, name: "解聘信息", path: "/Hr-index/decruitment"},
            {id: 121, name: "解聘教师端", path: "/Hr-index/jpteacher"}
          ]
        },
        {
          id: 3,
          name: "劳资管理",
          path: "",
          icon: "icon_hrLabour.png",
          children: [
            {id: 117, name: "劳资详情", path: "/Hr-index/labour/details"},
            {
              id: 118,
              name: "岗位劳资设定",
              path: "/Hr-index/labour/setting"
            }
          ]
        },
        {
          id: 4,
          name: "考勤管理",
          path: "/Hr-index/check/manage",
          icon: "icon_manage.png"
        },
        {
          id: "5",
          name: "培训管理",
          path: "/Hr-index/modlifyift",
          icon: "icon_modifyift.png"
        },
        {
          id: "6",
          name: "离岗创业管理",
          path: "/Hr-index/Quit",
          icon: "icon_dimission.png"
        },
        {
          id: "7",
          name: "护照管理",
          icon: "icon_Passport.png",
          path: "/Hr-index/Passport"
        },
        {
          id: "8",
          name: "权限管理",
          icon: "icon_jurisdiction_li.png",
          path: "",
          children: [
            {id: "115", name: "人员管理", path: "/Hr-index/Jurisdiction_set"},
            {id: "116", name: "角色管理", path: "/Hr-index/Jurisdiction_role"}
          ]
        },
        {
          id: "11",
          name: "院系专业管理",
          path: "/Hr-index/yxhome",
          icon: "icon_yxhome.png"
        },
        {
          id: "",
          name: "课程管理",
          path: "/Hr-index/KcAdministration",
          icon: "icon_KcAdministration.png"
        },
        {
          id: "9",
          name: "个人信息",
          icon: "icon_Personal_li.png",
          path: "",
          children: [
            {
              id: "111",
              name: "个人档案rerwerwerwerwerwerwerwerwerwerwerwerwerwerwerwer",
              path: "/Hr-index/Personal_file"
            },
            {id: "112", name: "个人考勤", path: "/Hr-index/Personal_check"},
            {id: "113", name: "劳资详情", path: "/Hr-index/Personal_labour"},
            {id: "114", name: "培训详情", path: "/Hr-index/Personal_train"}
          ]
        }
      ], //导航数组
    }
  }
}
</script>
<style>

.el-aside::-webkit-scrollbar {
  width: 4px;
  background: #00d2ca;
}

.el-aside::-webkit-scrollbar-thumb {
  background: #009d97;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
  border-bottom-right-radius: 10px;
  border-bottom-left-radius: 10px;
}

.el-main::-webkit-scrollbar {
  display: none;
}

.el-aside {
  text-align: center;
  position: absolute;
  top: 80px;
  bottom: 0;
  left: 0;
  background-color: #00bfb8 !important;
  min-height: 800px;

.el-menu-item-group /deep/ .el-menu-item-group__title {
  padding: 0 !important;
}

.el-menu-item:hover {
  background-color: #00d2ca;
}

.child_li {
  color: #ffff;
  display: flex;
  align-items: center;
  padding: 0;

span:first-child {
  margin-left: 23px;
}

span:last-child {
  margin-left: 23px;
}

}
}

</style>