<template>

  <div>
    <div class="p_c_box-flex_col">
      <!--      <el-tree-->
      <!--          :data="data"-->
      <!--          node-key="id"-->
      <!--          default-expand-all-->
      <!--          @node-drag-start="handleDragStart"-->
      <!--          @node-drag-enter="handleDragEnter"-->
      <!--          @node-drag-leave="handleDragLeave"-->
      <!--          @node-drag-over="handleDragOver"-->
      <!--          @node-drag-end="handleDragEnd"-->
      <!--          @node-drop="handleDrop"-->
      <!--          draggable-->
      <!--          :allow-drop="allowDrop"-->
      <!--          :allow-drag="allowDrag"-->
      <!--      >-->
      <!--      </el-tree>-->
      <div v-for="(value,index) in data">
        value

      </div>
    </div>
    <div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          name: "cunzai",
          child: [
            {
              name: "ren",
              child: [
                {
                  name: "情感",
                  child: []
                }
              ]
            }

          ],
        }
      ],
    }
  }
}
</script>