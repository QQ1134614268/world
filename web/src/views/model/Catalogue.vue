<template>
  <div>
    <el-tree
        :data="data"
        node-key="id"
        default-expand-all
        :label="name"
        :expand-on-click-node="false">
      <span class="custom-tree-node" slot-scope="{ node, data }">
        <span>
        {{ data.name }}
        </span>
        <span>
          <el-button
              type="text"
              size="mini"
              @click="() => append(data)">
            Append
          </el-button>
          <el-button
              type="text"
              size="mini"
              @click="() => remove(node, data)">
            Delete
          </el-button>
        </span>
      </span>
    </el-tree>
  </div>
</template>

<script>
export default {
  name: "Catalogue",
  data() {
    return {
      data2: [
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
      ],
      data:JSON.parse(JSON.stringify([
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
      ])),
    }
  },
  methods: {
    append(data) {
      const newChild = {id: id++, label: 'testtest', children: []};
      if (!data.children) {
        this.$set(data, 'children', []);
      }
      data.children.push(newChild);
    },

    remove(node, data) {
      const parent = node.parent;
      const children = parent.data.children || parent.data;
      const index = children.findIndex(d => d.id === data.id);
      children.splice(index, 1);
    },
  }
}
</script>

<style scoped>

</style>