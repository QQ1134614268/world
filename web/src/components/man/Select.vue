<template>
  <div>
<!--todo 查找,排序,导出,  分页-->
    <section>
      <el-button>新增</el-button>
      <el-button>搜索</el-button>
    </section>
    <el-table :data="tableData"></el-table>
    <el-dialog :title="form.id?'编辑':'新增'" :visible.sync="dialogVisible">
      <el-form ref="form" :model="form" style="padding: 1rem">
        <el-form-item label="取值">
          <el-input v-model="form.value"></el-input>
        </el-form-item>
        <el-form-item label="分组">
          <el-input v-model="form.group_code"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
          <el-button type="primary" @click="onCancel">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "Select",
  data() {
    return {
      form: {},
      dialogVisible: false
    }
  },
  methods: {
    onSubmit() {
    },
    onCancel() {
    }
  },
  props: {
    tableData: Array
  },
}
</script>

<style scoped>

</style>