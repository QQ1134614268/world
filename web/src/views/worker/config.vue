<template>
  <div>
    <div class="p_c_flexbox_row">
      <el-menu default-active="1" active-text-color="#409EFF">
        <el-menu-item index="1">
          <el-button @click="group='BUILD'; init()">楼层</el-button>
        </el-menu-item>
        <el-menu-item index="2">
          <el-button @click="group='WORK_TYPE'; init()"> 工作类型</el-button>
        </el-menu-item>
        <el-menu-item index="3">
          <el-button @click="group='BUILD_LEADER'; init()">工长</el-button>
        </el-menu-item>
      </el-menu>
      <div>
        <div>
          <el-button @click="add();editDialog=true">增加</el-button>
        </div>
        <el-table :data="data">
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
        <el-form-item label="编码">
          <el-input class="col-6" v-model="form.code"></el-input>
        </el-form-item>
        <el-form-item label="枚举值">
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
import {ConfigApi} from "@/api/const";

export default {
  name: "config",
  data() {
    return {
      options: [],
      value: '',
      editDialog: false,
      url: ConfigApi,
      data: [],
      parent_id: -1,
      form: {},
      group: 'BUILD'
    }
  },
  methods: {
    async init() {
      let data = {"group_code": this.group}
      let res = await this.$get2(this.url, 0, data)
      this.data = res.data.data
    },
    async save() {
      let res;
      this.form["group_code"] = this.group
      if (this.form.id) {
        res = await this.$putJson2(ConfigApi, 0, this.form)
      } else {
        res = await this.$postJson2(ConfigApi, this.form.id, this.form)
      }
      if (res.data.code == 1) {
        this.$message.info("操作成功")
      } else {
        this.$message.info("编辑失败")
      }
    },
    async add() {
      this.form = {}
    },
    async handleChange() {

    },
    handleEdit(index, row) {
      this.form = row;
      this.editDialog = true
    },
    async handleDelete(row) {
      let res = await this.$deleteJson2(ConfigApi, 0, row.id)
      if (res.data.code == 1) {
        this.$message.info("操作成功")
      } else {
        this.$message.info(res.data.data)
      }
    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>