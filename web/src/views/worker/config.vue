<template>
  <div>

    <div>
      <el-button @click="add">增加</el-button>
    </div>
    <div class="p_c_flexbox">
      <div>
        <el-cascader v-model="value" :options="options" @change="handleChange"></el-cascader>
      </div>
      <div>
        <el-button @click="init">搜索</el-button>
      </div>
    </div>
    <el-table :data="data">
      <el-table-column prop="code" label="编码" sortable></el-table-column>
      <el-table-column prop="value" label="枚举值" sortable></el-table-column>
      <el-table-column prop="comment" label="备注" sortable></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "config",
  data() {
    return {
      url: "/api/config_api/ConfigApi",
      data: [],
      parent_id: -1,
    }
  },
  methods: {
    async init() {
      let data = {"parent_id": this.parent_id}
      let res = await this.$get2(this.url, 0)
      this.data = res.data.data
    },
    async add() {
      let res = await this.$get2(this.url, 0)
      this.data = res.data.data
    },
    async handleChange() {


    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>