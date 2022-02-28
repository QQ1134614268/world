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
      标签
<!--      <section>-->
<!--        <el-button v-for="list"> </el-button>-->
<!--      </section>-->

      <section>

      </section>
    </main>
  </div>
</template>

<script>
import {ProveApi, SystemLevelApi} from "@/api/api";

export default {
  name: "SystemLevel",
  data() {
    return {

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