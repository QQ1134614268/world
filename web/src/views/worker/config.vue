<template>
  <div>
    <div class="p_c_flexbox_row">
<!--      <el-dropdown>-->
<!--  <span class="el-dropdown-link">-->
<!--    下拉菜单<i class="el-icon-arrow-down el-icon&#45;&#45;right"></i>-->
<!--  </span>-->
<!--        <el-dropdown-menu slot="dropdown">-->
<!--          <el-dropdown-item>黄金糕</el-dropdown-item>-->
<!--          <el-dropdown-item>狮子头</el-dropdown-item>-->
<!--          <el-dropdown-item>螺蛳粉</el-dropdown-item>-->
<!--        </el-dropdown-menu>-->
<!--      </el-dropdown>-->
      <el-menu default-active="1" active-text-color="#409EFF">
        <el-menu-item index="1" @click="group='BUILD'; init()">
          楼层
        </el-menu-item>
        <el-menu-item index="2" @click="group='WORK_TYPE'; init()">
          工作类型
        </el-menu-item>
      </el-menu>
      <div class='col-12'>
        <div>
          <el-button @click="add();editDialog=true">增加</el-button>
        </div>
        <el-table :data="data" class='col-6'>
          <el-table-column prop="value" label="取值"></el-table-column>
          <el-table-column prop="comment" label="备注"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="editDialog" width="30%">
      <el-form v-model="form">
        <el-form-item label="取值">
          <el-input class="col-6" v-model="form.value"></el-input>
        </el-form-item>
        <el-form-item label="备注">
          <el-input class="col-6" v-model="form.comment"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button @click="editDialog = false">取 消</el-button>
          <el-button type="primary" @click="save();editDialog = false">保存</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import {ConfigApi} from "@/api/api";
import {deleteJson2, get2, postJson2, putJson2} from "@/api/http";

export default {
  name: "config",
  data() {
    return {
      options: [],
      value: '',
      editDialog: false,
      data: [],
      form: {},
      group: 'BUILD'
    }
  },
  methods: {
    async init() {
      let data = {"group_code": this.group}
      let res = await get2(ConfigApi, 0, data)
      this.data = res.data.data
    },
    async save() {
      let res;
      this.form["group_code"] = this.group
      if (this.form.id != undefined) {
        res = await putJson2(ConfigApi, this.form.id, this.form)
      } else {
        let data = {
          group_code: this.form["group_code"],
          value: this.form["value"],
          comment: this.form["comment"],
        }
        res = await postJson2(ConfigApi, 0, data)
      }
      if (res.data.code == 1) {
        this.$message.info("操作成功")
      } else {
        this.$message.info("编辑失败")
      }
      await this.init()
    },
    async add() {
      this.form = {}
    },
    handleEdit(index, row) {
      this.form = row;
      this.editDialog = true
    },
    async handleDelete(row) {
      let res = await deleteJson2(ConfigApi, 0, row.id)
      if (res.data.code == 1) {
        this.$message.info("操作成功")
      } else {
        this.$message.info(res.data.data)
      }
      await this.init()
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>