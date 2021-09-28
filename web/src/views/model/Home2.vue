<template>
  <div class="p_c_flexbox_row">
    <div class="col-3">
      <el-tree
          :data="data"
          node-key="id"
          default-expand-all
          draggable
      >

        <!--          @node-drag-start="handleDragStart"-->
        <!--          @node-drag-enter="handleDragEnter"-->
        <!--          @node-drag-leave="handleDragLeave"-->
        <!--          @node-drag-over="handleDragOver"-->
        <!--          @node-drag-end="handleDragEnd"-->
        <!--          @node-drop="handleDrop"-->
        <!--          :allow-drop="allowDrop"-->
        <!--          :allow-drag="allowDrag"-->
        <template #default="{ node, data }">
        <span class="custom-tree-node">
          <span>{{ node.label }}</span>
          <span>
            <a @click="append(data)"> Append </a>
            <a @click="remove(node, data)"> Delete </a>
          </span>
        </span>
        </template>
      </el-tree>
    </div>
    <div class="col-9">
      content
      <div class="title">
        人
        <div class="H1">
          H1 - 论点一
          <div class="H2">
            证明
          </div>
          <div class="H2">
            现象
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          id: 1,
          label: '一级 1',
          children: [
            {
              id: 4,
              label: '二级 1-1',
              children: [
                {
                  id: 9,
                  label: '三级 1-1-1',
                },
                {
                  id: 10,
                  label: '三级 1-1-2',
                },
              ],
            },
          ],
        },
        {
          id: 2,
          label: '一级 2',
          children: [
            {
              id: 5,
              label: '二级 2-1',
            },
            {
              id: 6,
              label: '二级 2-2',
            },
          ],
        },
        {
          id: 3,
          label: '一级 3',
          children: [
            {
              id: 7,
              label: '二级 3-1',
            },
            {
              id: 8,
              label: '二级 3-2',
              children: [
                {
                  id: 11,
                  label: '三级 3-2-1',
                },
                {
                  id: 12,
                  label: '三级 3-2-2',
                },
                {
                  id: 13,
                  label: '三级 3-2-3',
                },
              ],
            },
          ],
        },
      ],
      defaultProps: {
        children: 'children',
        label: 'label',
      },
    }
  },
  methods: {
    append(data) {
      const newChild = {id: id++, label: 'testtest', children: []}
      if (!data.children) {
        data.children = []
      }
      data.children.push(newChild)
      this.data = [...this.data]
    },

    remove(node, data) {
      const parent = node.parent
      const children = parent.data.children || parent.data
      const index = children.findIndex((d) => d.id === data.id)
      children.splice(index, 1)
      this.data = [...this.data]
    },
    // handleDragStart(node, ev) {
    //   console.log('drag start', node)
    // },
    // handleDragEnter(draggingNode, dropNode, ev) {
    //   console.log('tree drag enter: ', dropNode.label)
    // },
    // handleDragLeave(draggingNode, dropNode, ev) {
    //   console.log('tree drag leave: ', dropNode.label)
    // },
    // handleDragOver(draggingNode, dropNode, ev) {
    //   console.log('tree drag over: ', dropNode.label)
    // },
    // handleDragEnd(draggingNode, dropNode, dropType, ev) {
    //   console.log('tree drag end: ', dropNode && dropNode.label, dropType)
    // },
    // handleDrop(draggingNode, dropNode, dropType, ev) {
    //   console.log('tree drop: ', dropNode.label, dropType)
    // },
    // allowDrop(draggingNode, dropNode, type) {
    //   if (dropNode.data.label === '二级 3-1') {
    //     return type !== 'inner'
    //   } else {
    //     return true
    //   }
    // },
    // allowDrag(draggingNode) {
    //   return draggingNode.data.label.indexOf('三级 3-2-2') === -1
    // },
  },
}
</script>

<style>

</style>
