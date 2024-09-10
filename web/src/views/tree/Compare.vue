<template>
  <div class="tree-drag">
    <!--    <el-autocomplete class="inline-input" v-model="search" placeholder="请输入内容" :fetch-suggestions="querySearch"-->
    <!--                     :trigger-on-focus="false" @select="handleSelect">-->
    <!--    </el-autocomplete>-->

    <!--    <el-autocomplete class="inline-input" v-model="search" placeholder="请输入内容" :fetch-suggestions="querySearch2"-->
    <!--                     :trigger-on-focus="false" @select="handleSelect2">-->
    <!--    </el-autocomplete>-->
    <div class="p_c_flexbox_row">
      <div class="col-6">
        <el-tree lazy :load="load" :props="props" :data="treeData1" ref="treeIn" class="tree" node-key="id"
                 draggable @node-drag-start="handleDragstart" @node-drag-end="handleDragend">
        </el-tree>
      </div>
      <div class="col-6">
        <el-tree lazy :load="load2" :props="props" :data="treeData2" ref="treeOut" node-key="id"
                 draggable @node-drop="handleDrop">
        </el-tree>
      </div>
    </div>

  </div>
</template>
<script>
import {ProveApi, ProveBlueprintApi_contain_value} from "@/api/api";
import {get2, putJson2} from "@/api/http";

export default {
  name:'CompareComponent',
  data() {
    return {
      search: "",
      search2: "",
      treeData1: [],
      treeData2: [],
      searchFlag: "",
      searchFlag2: "",
      parent_id: "",
      parent_id2: "",
      splitRules: "",
      splitRules2: "",
      props: {
        label: 'value',
        children: 'zones',
      },
    };
  },
  methods: {
    async querySearch(queryString, callback) {
      let paras = {value: queryString}
      let res = await get2(ProveBlueprintApi_contain_value, 0, paras)
      this.splitRules = res.data.data
      callback(this.splitRules)
    },
    async querySearch2(queryString, callback) {
      let paras = {value: queryString}
      let res = await get2(ProveBlueprintApi_contain_value, 0, paras)
      this.splitRules2 = res.data.data
      callback(this.splitRules2)
    },
    async handleSelect(item) {
      this.parent_id = item.id
      this.searchFlag = !this.searchFlag
    },
    async handleSelect2(item) {
      this.parent_id2 = item.id
      this.searchFlag2 = !this.searchFlag2
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
    async load2(node, resolve) {
      let paras = {}
      if (node.level === 0) {
        paras = {parent_id: this.parent_id2}
      } else {
        paras = {parent_id: node.data.id}
      }
      let res = await get2(ProveApi, 0, paras)
      resolve(res.data.data)
    },
    //左侧节点触发拖拽
    handleDragstart(node, event) {
      //在左侧节点触发拖拽的时候触发右侧节点的拖拽事件
      this.$refs.treeOut.$emit('tree-node-drag-start', event, {node: node});
    },
    //拖拽结束，但是确定是否成功
    handleDragend(draggingNode, endNode, position, event) {
      // 新的空节点
      let newData = {id: (+new Date), children: []};
      //在左tree插入拖拽的节点
      this.$refs.treeIn.insertBefore(newData, draggingNode);
      //右tree触发结束拖拽事件
      this.$refs.treeOut.$emit('tree-node-drag-end', event);
      this.$nextTick(() => {
        // 如果是移动到了自身---
        if (this.$refs.treeIn.getNode(draggingNode.data)) {
          this.$refs.treeIn.remove(newData);
        } else {
          // 如果移动到了右tree上----
          let data = JSON.parse(JSON.stringify(draggingNode.data));
          this.$refs.treeIn.insertAfter(data, this.$refs.treeIn.getNode(newData));
          this.$refs.treeIn.remove(newData);
          console.log('移动到别的tree')
        }
      })
    },
    async handleDrop(draggingNode, dropNode, dropType, ev) {
      if (dropType === "inner") {
        draggingNode.data.parent_id = dropNode.data.id
      }
      if (dropType === "after") {
        draggingNode.data.parent_id = dropNode.data.parent_id
      }
      if (dropType === "before") {
        draggingNode.data.parent_id = dropNode.data.parent_id
      }
      let res3 = await putJson2(ProveApi, draggingNode.data.id, draggingNode.data);
      if (res3.data.code !== 1) {
        this.$message.error(res3.data.data);
      }
    },
  }
};
</script>

<style scoped>

</style>
