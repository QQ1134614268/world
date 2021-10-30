<template>
  <div>
    <el-tree :data="data" lazy :load="load" :props="props">
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
  },
}
</script>

<style scoped>

</style>