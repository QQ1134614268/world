<template>
  <div>
    平台商品
    <div v-for="(o,index) in data " class="p_c_flexbox">
      <div style="width: 20rem;">
        <div>
          <img :src="o.img" style="object-fit: cover">
        </div>
        <div>
          <div>
            价格{{ o.price }}
          </div>
          <div>
            介绍
          </div>
          <div>
            <el-button>caozuo</el-button>
          </div>
        </div>
      </div>
    </div>
    <div>
      <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
        购物车
      </el-button>
      <el-button @click="buy"> 结算</el-button>
    </div>
    <el-drawer title="购物车" :visible.sync="drawer" direction='btt'>
      <el-table :data="order_list" style="width: 100%">
        <el-table-column prop="name" label="商品名" width="180"></el-table-column>
        <el-table-column prop="price" label="商品价格"></el-table-column>
        <el-button @click="buy"> 结算</el-button>
        <el-table-column prop="num" label="数量" width="180"></el-table-column>
      </el-table>
    </el-drawer>
  </div>
</template>

<script>
export default {
  name: "market",
  data() {
    return {
      data: [],
      drawer: false,
      order_list: [],
    }
  },
  methods: {
    buy() {
    },
    init() {

    }
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>