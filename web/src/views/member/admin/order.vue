<template>
  <div>
    订单(搜索)
    <el-table>

    </el-table>
  </div>
</template>

<script>
import {OrderApi} from "@/api/api";

export default {
  name: "order",
  data() {
    return {
      url: "",
      data: [],
    }
  },
  methods: {
    async init() {
      let data = {}
      let res = await this.$get2(OrderApi, 0, data)
      if (res.data.code != 1) {
        this.$message('服务器异常');
        return
      }
      this.data = res.data.data
    }
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>