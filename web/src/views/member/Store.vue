<template>
  <div style="display: flex;">
    <div style="width: 20rem">
      <div>
        <el-button @click="showCtl('a')"> 商品列表</el-button>
      </div>
      <div>
        <el-button @click="showCtl('b')"> 会员列表</el-button>
      </div>
    </div>
    <div style="width: 100%">
      <div v-if="ctl.a">
        <Goods></Goods>
      </div>
      <div v-if="ctl.b">
        <el-table :data="memberList">

        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import Goods from "@/views/member/Goods";

export default {
  name: "Store",
  components: {Goods},
  data() {
    return {
      memberList: [],
      form: {},
      tableData: [],
      ctl: {
        a: true
      },
      store_id: ""
    };
  },
  methods: {
    showCtl(arg) {
      this.ctl = {}
      this.ctl[arg] = true
    },
    async handleEdit(index, row) {
      this.showCtl('b')
      this.form = row
    },
  },
  created() {
  }
}
</script>

<style scoped>


</style>
