<template>
  <div>
    <div>
      <router-link :to="{name:'/model/Compare'}">
        <el-button>移动</el-button>
      </router-link>
    </div>
    <div>
      <el-autocomplete class="inline-input" v-model="search" placeholder="请输入内容" :fetch-suggestions="querySearch"
                       :trigger-on-focus="false" @select="handleSelect">
      </el-autocomplete>
    </div>
    <div>
      <el-tree ref="treeIn" :data="data" lazy :load="load" :props="props" :default-expanded-keys="idArr"
               node-key="id"
               @node-drop="handleDrop"
               draggable
               v-if="searchFlag"
      >
      <span class="custom-tree-node" slot-scope="{ node, data }">
        <router-link tag="a" target="_blank" :to="{name:'/model/Book',query: {id: data.id}}">
              {{ data.value }}
        </router-link>
      </span>
      </el-tree>
    </div>
    <div>
      <el-tree ref="treeIn" :data="data" lazy :load="load" :props="props" :default-expanded-keys="idArr"
               node-key="id"
               @node-drop="handleDrop"
               draggable
               v-if="!searchFlag"
      >
      <span class="custom-tree-node" slot-scope="{ node, data }">
        <router-link :to="{name:'/model/Book',query: {id: data.id}}">
              {{ data.value }}
        </router-link>
      </span>
      </el-tree>
    </div>
  </div>
</template>

<script>
export default {
  name: "Catalogue",
  data() {
    return {
      searchFlag: true,
      splitRules: [{id: 1, value: 122}, {value: 122}, {value: 122}],
      search: "",
      parent_id: 0,
      url: "/api/model_api/ProveApi",
      url2: "/api/model_api/Prove2Api",
      data: [],
      idArr: [1],
      // idArr: [1, 2, 3],
      props: {
        label: 'value',
        children: 'zones',
      },
    }
  },
  methods: {
    async querySearch(queryString, callback) {
      let paras = {value: queryString}
      let res = await this.$get2(this.url2, 0, paras)
      this.splitRules = res.data.data
      callback(this.splitRules)
    },
    async handleSelect(item) {
      this.parent_id = item.id
      this.searchFlag = !this.searchFlag
    },
    async load(node, resolve) {
      let paras = {}
      if (node.level == 0) {
        paras = {parent_id: this.parent_id}
      } else {
        paras = {parent_id: node.data.id}
      }
      let res = await this.$get2(this.url, 0, paras)
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
      let res3 = await this.$putJson2(this.url, draggingNode.data.id, draggingNode.data);
    },
  },
}
</script>

<style scoped>

</style>