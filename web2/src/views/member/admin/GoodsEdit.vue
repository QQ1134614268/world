<template>
  <div>
    <el-form>
      <el-form-item label="账号">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "GoodsEdit",
  data() {
    return {
      form: {}
    }
  }
}
</script>

<style scoped>

</style>