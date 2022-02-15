<template>
  <div>
    <div class="block">
      <router-link tag="a" target="_blank" :to="{path:'/tree/Compare'}" class="p_c_space">
        移动
      </router-link>
      <router-link tag="a" target="_blank" :to="{path:'/tree/Parent'}" class="p_c_space">
        查看父级
      </router-link>
      <router-link tag="a" target="_blank" :to="{path:'/tree/Story'}" class="p_c_space">
        故事
      </router-link>
      <router-link tag="a" target="_blank" :to="{path:'/tree/MuchChildren'}" class="p_c_space">
        子节点多告警
      </router-link>
      <router-link tag="a" target="_blank" :to="{path:'/tree/PopularWord'}" class="p_c_space">
        关注与常用
      </router-link>
      <router-link tag="a" target="_blank" :to="{path:'/tree/KeyWord'}" class="p_c_space">
        关键词统计
      </router-link>
      <router-link tag="a" target="_blank" :to="{path:'/FeedBack'}" class="p_c_space">
        反馈
      </router-link>
      <router-link tag="a" target="_blank"
                   :to="{path:'/tree/AddProve',query: {id:0,value: '新项目'}}"
                   class="p_c_space">
        创建新项目
      </router-link>

    </div>
    <div class="block">
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
        <router-link tag="a" target="_blank" :to="{path:'/tree/Book',query: {id: data.id}}">
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
        <router-link tag="a" target="_blank" :to="{path:'/tree/Book',query: {id: data.id}}">
              {{ data.value }}
        </router-link>
      </span>
      </el-tree>
    </div>
  </div>
</template>

<script>
import {ProveApi, ProveBlueprintApi_contain_value} from "@/api/api";

export default {
  name: "Catalogue",
  data() {
    return {
      searchFlag: true,
      splitRules: [{id: 1, value: 122}, {value: 122}, {value: 122}],
      search: "",
      parent_id: 0,
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
      let res = await this.$get2(ProveBlueprintApi_contain_value, 0, paras)
      this.splitRules = res.data.data
      callback(this.splitRules)
    },

    async handleSelect(item) {
      this.parent_id = item.parent_id
      this.searchFlag = !this.searchFlag
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
}
</script>

<style scoped>

</style>