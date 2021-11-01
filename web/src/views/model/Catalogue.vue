<template>
  <div>
    <el-tree :data="data" lazy :load="load" :props="props" :default-expanded-keys="idArr"
             node-key="id"
             @node-drop="handleDrop"
             draggable
    >
      <span class="custom-tree-node" slot-scope="{ node, data }">
        <router-link :to="{name:'/model/Book',query: {id: data.id}}">
              {{ data.value }}
        </router-link>
      </span>
    </el-tree>
  </div>
</template>

<script>
export default {
  name: "Catalogue",
  data() {
    return {
      url: "/api/model_api/ProveApi",
      data: [],
      idArr: [1, 2, 3],
      props: {
        label: 'value',
        children: 'zones',
      },
    }
  },
  methods: {
    async load(node, resolve) {
      let child_data = await this.getData(node.data, node.data.id)
      resolve(child_data)
    },
    async getData(data, parent_id) {
      if (parent_id == null) {
        parent_id = 0
        data = this.data
      }
      let paras = {parent_id: parent_id}
      let res = await this.$get2(this.url, 0, paras)
      return res.data.data
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
      let res3 = await this.$putJson2(this.url, draggingNode.data.id, draggingNode.data);
    },
  },
}
</script>

<style scoped>

</style>