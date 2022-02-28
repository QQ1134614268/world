<template>
  <div class="p_c_HolyGrail-body" style="height: 100%; ">
    <div class="p_c_box-flex" style="overflow-y: scroll">
      <nav class="p_c_box-flex_col">
        <a :href="'#'+obj.label" :key="index" v-for="(obj,index) in tableData">{{ obj.label }}</a>
      </nav>
      <div>
        <div :key="index" v-for="(obj,index) in tableData" style="height: 50rem">
          <a :id="obj.label" style="height: 1.6rem; font-weight: bold">{{ obj.label }}</a>
          <div :key="index2" v-for="(obj2, index2) in obj.data" class="p_c_box-flex">
            <el-image style="width: 5rem" :src="obj2.images"></el-image>
            <div>
              <div>
                {{ obj2.name }}
              </div>
              <div>
                售价: {{ obj2.price }}
                <el-input-number v-model="obj2.num" @change="handleChange(obj2)" :min="0" :max="10" size="small"
                                 label="描述文字"></el-input-number>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
      <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
        购物车
      </el-button>
      <section v-show="drawer">
        <el-table :data="order_list" style="width: 100%">
          <el-table-column prop="name" label="商品名" width="180"></el-table-column>
          <el-table-column prop="price" label="商品价格"></el-table-column>
          <el-table-column prop="num" label="数量" width="180">
            <template slot-scope="scope">
              <el-input-number v-model="scope.row.num" :min="0" :max="10" size="small"></el-input-number>
            </template>
          </el-table-column>
        </el-table>
        <el-button @click="buy">下单</el-button>
      </section>
    </div>
  </div>
</template>

<script>
import {GoodsApi} from "@/api/api";
import {toTree} from "@/api/util";
import {postOrder} from "@/api/member_api";

export default {
  name: "Store",
  data() {
    return {
      num: 0,
      tableData: [],
      drawer: false,
      order_list: [],
      orderMap: {},
      store_id: 1
    }
  },
  methods: {
    buy() {
      postOrder(this.order_list)
    },
    handleChange(goodObj) {
      this.orderMap[goodObj.id] = goodObj
      this.order_list = []
      for (let i in this.orderMap) {
        this.order_list.push(this.orderMap[i])
      }
    },
    async init() {
      let data = {
        store_id: this.store_id
      }
      let response = await this.$get2(GoodsApi, 0, data);
      this.tableData = response.data.data
      this.tableData = toTree(this.tableData)
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>