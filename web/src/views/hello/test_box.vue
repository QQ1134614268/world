<template>
  <div>
    <div class="btn_box">
      <div class="row">
        <span>方向</span>
        <el-radio-group v-model="radio">
          <el-radio :label="3">备选项</el-radio>
          <el-radio :label="6">备选项</el-radio>
          <el-radio :label="9">备选项</el-radio>
        </el-radio-group>
      </div>

      <div class="row">
        <span>成长</span>
        <el-radio-group v-model="radio">
          <el-radio :label="3">备选项</el-radio>
          <el-radio :label="6">备选项</el-radio>
          <el-radio :label="9">备选项</el-radio>
        </el-radio-group>
      </div>

      <div class="row">
        <span>对齐</span>
        <el-radio-group v-model="radio">
          <el-radio :label="3">备选项</el-radio>
          <el-radio :label="6">备选项</el-radio>
          <el-radio :label="9">备选项</el-radio>
        </el-radio-group>
      </div>
    </div>

    <div class="items_container">
      <div class="class_sig" v-for="item of data" :style="{width:item.width, height:item.height}">
        {{ item.value }}
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "test_box",
  data() {
    return {
      radio: "",
      items_cntr: {},
      data: [
        {value: 1, width: '6rem', height: '6rem'},
        {value: 2, width: '5rem', height: '2rem'},
        {value: 3, width: '5rem', height: '2rem'},
        {value: 4, width: '5rem', height: '2rem'},
        {value: 5, width: '5rem', height: '2rem'},
        {value: 6, width: '5rem', height: '2rem'},
        {value: 7, width: '5rem', height: '2rem'},
      ]
    }
  }
}
</script>

<style scoped>
.btn_box {

}

.items_container {

}

.class_sig {

}
</style>
