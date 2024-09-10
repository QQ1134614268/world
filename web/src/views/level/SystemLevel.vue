<template>
  <div class="p_c_box-flex">
    <nav class="col-4">
      <el-tree ref="treeIn" :data="treeData" lazy :load="load" :props="props"
               node-key="id"
               draggable
      >
      <span class="custom-tree-node" slot-scope="{ node, data }">
       {{ data.value }}
      </span>
      </el-tree>
    </nav>
    <main class="col-8">
      <!--      <span>标签</span>-->
      <!--      <section>-->
      <!--        <el-button v-for="list"> </el-button>-->
      <!--      </section>-->

      <section>
        <el-button size="mini" type="danger" @click="dialogVisible=true;form={}">新增</el-button>
        <el-button size="mini" type="danger" @click="dialogVisible=true;form={}">导出css</el-button>
        <el-table :data="list">
          <el-table-column prop="value" sortable label="取值"></el-table-column>
          <el-table-column prop="group_code" sortable label="分组"></el-table-column>
          <el-table-column prop="" sortable label="函数表达式">50%(9)</el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" type="danger" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </section>
    </main>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" label-width="8rem" style="padding: 1rem">
        <el-form-item label="取值">
          <el-input class="col-6" v-model="form.value"></el-input>
        </el-form-item>
        <el-form-item label="分组">
          <el-input class="col-6" v-model="form.group_code"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button type="primary" @click="onCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import {ProveApi, SystemLevelApi} from "@/api/api";
import {deleteJson2, get2, ppJson} from "@/api/http";

export default {
  name: "SystemLevel",
  data() {
    return {
      dialogVisible: false,
      form: {},
      list: [],
      parent_id: -1,

      splitRules: [],
      search: "",
      treeData: [],
      idArr: [1],
      props: {
        label: 'value',
        children: 'zones',
      },
    }
  },
  methods: {
    async onSubmit() {
      let response = await ppJson(SystemLevelApi, this.form.id, this.form);
      if (response.data.code !== 1) {
        this.$message.error(response.data.data);
      }
      this.dialogVisible = false
    },
    onCancel() {
      this.dialogVisible = false
    },
    handleEdit(row) {
      this.form = row
      this.dialogVisible = true
    },
    async handleDelete() {
      let response = await deleteJson2(SystemLevelApi, this.form.id);
      if (response.data.code !== 1) {
        this.$message.error(response.data.data);
      }
    },
    async init() {
      let data = {
        parent_id: this.parent_id
      }
      let response = await get2(SystemLevelApi, 0, data);
      this.list = response.data.data
    },
    async load(node, resolve) {
      let paras = {}
      if (node.level === 0) {
        paras = {parent_id: this.parent_id}
      } else {
        paras = {parent_id: node.data.id}
      }
      let res = await get2(ProveApi, 0, paras)
      resolve(res.data.data)
    },
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>