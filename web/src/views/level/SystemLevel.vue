<template>
  <div class="p_c_box-flex">
    <nav class="col-4">
      <el-tree ref="treeIn" :data="treeData" lazy :load="load" :props="props"
               node-key="id"
               @node-drop="handleDrop"
               draggable
      >
      <span class="custom-tree-node" slot-scope="{ node, data }">
       {{ data.value }}
      </span>
      </el-tree>
    </nav>
    <main>
      <span>标签</span>
      <!--      <section>-->
      <!--        <el-button v-for="list"> </el-button>-->
      <!--      </section>-->

      <section>
        <el-table :data="list">
          <el-table-column prop="name" sortable label="地点"></el-table-column>
          <el-table-column prop="group_code" sortable label="分组"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" type="danger" @click="dialogVisible=true;form={}">新增</el-button>
              <el-button size="mini" type="danger" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </section>
    </main>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" :rules="rules" label-width="8rem" style="padding: 1rem">
        <el-form-item label="描述">
          <el-input v-model="form.describe"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即创建</el-button>
          <el-button type="primary" @click="onCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import {ProveApi, SystemLevelApi} from "@/api/api";

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
    onSubmit() {
    },
    onCancel() {
    },
    handleEdit() {
    },
    handleDelete() {
    },
    async init() {
      let data = {
        parent_id: this.parent_id
      }
      let response = await this.$get2(SystemLevelApi, 0, data);
      this.list = response.data.data
    },
    async load(node, resolve) {
      let paras = {}
      if (node.level == 0) {
        paras = {parent_id: this.parent_id}
      } else {
        paras = {parent_id: node.data.id}
      }
      let res = await this.$get2(ProveApi, 0, paras)
      resolve(res.data.data)
    },
    async handleDrop(draggingNode, dropNode, dropType, ev) {
      if (dropType == "inner") {
        draggingNode.data.parent_id = dropNode.data.id
      }
      if (dropType == "after") {
        draggingNode.data.parent_id = dropNode.data.parent_id
      }
      if (dropType == "before") {
        draggingNode.data.parent_id = dropNode.data.parent_id
      }
      let res3 = await this.$putJson2(ProveApi, draggingNode.data.id, draggingNode.data);
    },
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>