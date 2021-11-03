<template>
  <div>
    <div>
      <el-autocomplete class="inline-input" v-model="search" placeholder="请输入内容" :fetch-suggestions="querySearch"
                       :trigger-on-focus="false" @select="handleSelect">
      </el-autocomplete>
    </div>
    <el-tree :data="data" lazy :load="load" :props="props" :default-expanded-keys="idArr"
             node-key="id"
             @node-drop="handleDrop"
             draggable
             v-if="searchFlag"
    >
      <span class="custom-tree-node" slot-scope="{ node, data }">
        <router-link :to="{name:'/model/Book',query: {id: data.id}}">
              {{ data.value }}
        </router-link>
      </span>
    </el-tree>

    <div>---------------</div>
    <el-tree :data="data" lazy :load="load" :props="props" :default-expanded-keys="idArr"
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
      idArr: [1, 2, 3],
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
      // alert(queryString)
      callback(this.splitRules)
    },
    async handleSelect(item) {
      this.parent_id = item.id
      alert(this.parent_id)
      this.searchFlag = !this.searchFlag
    },
    async load(node, resolve) {
      if (node.level == 0) {
        alert(456)
        alert(this.parent_id)
        let child_data = await this.getData(node.data, this.parent_id)
        resolve(child_data)
        return
      }
      let child_data = await this.getData(node.data, node.data.id)
      resolve(child_data)
    },
    async getData(data, parent_id) {
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