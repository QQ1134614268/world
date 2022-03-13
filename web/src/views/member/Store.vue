<template>
  <div class="p_c_HolyGrail-body" style="height: 100%;">
    <div class="p_c_box-flex" style=" flex: 1">
      <nav class="p_c_box-flex_col">
        <a :href="'#'+obj.label" :key="index" v-for="(obj,index) in tableData">{{ obj.label }}</a>
      </nav>
      <div >
        <div :key="index" v-for="(obj,index) in tableData">
          <a :id="obj.label" style="color:#cccccc; font-weight: lighter">{{ obj.label }}</a>
          <div :key="index2" v-for="(obj2, index2) in obj.data" class="p_c_box-flex" style="margin-bottom: 0.5rem">
            <el-image style="width: 3rem;height: 3rem" :src="obj2.images"></el-image>
            <div class="p_c_box-flex_col" style="justify-content:space-between">
              <span>
                {{ obj2.name }}
              </span>
              <div class="p_c_flexbox_row">
                <span>售价: {{ obj2.price }}</span>
                <i class="el-icon-plus" @click="add(obj2)"
                   style="background-color: orangered; border-radius: 3rem;align-self: end"></i>
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
      tableData2: [],
      drawer: false,
      order_list: [],
      orderMap: {},
      store_id: 1
    }
  },
  methods: {
    add(obj) {
      obj.num = (obj.num || 0) + 1
      this.order_list = this.tableData2.filter((obj) => obj.num > 0)
    },
    buy() {
      postOrder(this.order_list)
    },
    async init() {
      let data = {
        store_id: this.store_id
      }
      let response = await this.$get2(GoodsApi, 0, data);
      this.tableData2 = response.data.data
      this.tableData = toTree(this.tableData2)
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped>

</style>