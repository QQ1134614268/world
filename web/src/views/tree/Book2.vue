<template>
  <div class="tree-drag">
    <el-tree :data="treeData1" ref="treeIn" class="tree" node-key="id" default-expand-all draggable
             :allow-drag="returnTrue" @node-drag-start="handleDragstart" @node-drag-end="handleDragend"></el-tree>
    <el-tree :data="treeData2" ref="treeOut" class="tree" node-key="id" default-expand-all draggable
             :allow-drop="returnTrue" @node-drop="handleDrop"></el-tree>
  </div>
</template>
<script>
export default {
  name: "Book2Component",
  data() {
    return {
      treeData1: [{
        id: 1,
        label: "1-1111",
        children: [{
          id: 4,
          label: "2-1111",
          children: [{id: 9, label: "3-1111"}]
        }],
      }],
      treeData2: [{
        id: 2,
        label: "1-2222",
        children: [{
          id: 5,
          label: "2-2222",
          children: [{id: 8, label: "3-2222"}],
        }],
      }],
    };
  },
  methods: {
    //左侧节点触发拖拽
    handleDragstart(node, event) {
      console.log('start', node, event)
      //在左侧节点触发拖拽的时候触发右侧节点的拖拽事件
      this.$refs.treeOut.$emit('tree-node-drag-start', event, {node: node});
    },
    //拖拽结束，但是确定是否成功
    handleDragend(draggingNode, endNode, position, event) {
      console.log('end', draggingNode, endNode, position, event)
      // 新的空节点
      let newData = {id: (+new Date), children: []};
      //在左tree插入拖拽的节点
      this.$refs.treeIn.insertBefore(newData, draggingNode);
      //右tree触发结束拖拽事件
      this.$refs.treeOut.$emit('tree-node-drag-end', event);
      this.$nextTick(() => {
        // 如果是移动到了自身---
        console.log(this.$refs.treeIn.getNode(draggingNode.data))
        if (this.$refs.treeIn.getNode(draggingNode.data)) {
          this.$refs.treeIn.remove(newData);
          console.log('移动到自身')
        } else {
          // 如果移动到了右tree上----
          let data = JSON.parse(JSON.stringify(draggingNode.data));
          this.$refs.treeIn.insertAfter(data, this.$refs.treeIn.getNode(newData));
          this.$refs.treeIn.remove(newData);
          console.log('移动到别的tree')
        }
      })
    },
    //结束拖拽，可得到拖拽来源与去向
    //  handleDrop(draggingNode, dropNode, dropType, ev) {
    //     console.log('移动结束',draggingNode, dropNode, dropType,ev);
    //   },
    returnTrue() {
      return true;
    },
    returnFalse() {
      return false;
    },
    handleDrop() {
    }
  }
};
</script>

<style scoped>
.tree {
  display: inline-block;
  overflow: hidden;
  width: 200px;
  height: 300px;
  border: 1px solid #444;
}
</style>
