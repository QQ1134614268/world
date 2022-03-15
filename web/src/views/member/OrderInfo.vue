<template>
  <div>
    <div v-for="(orderInfoVO,index) in tableData" class="p_c_flexbox_row">
      <img :src="orderInfoVO.goods_img" class="p_c_img_normal" style=""/>
      <div>
        {{ orderInfoVO.goods_name }}
      </div>
      <div>
        {{ orderInfoVO.num }}
      </div>
      <div>
        {{ orderInfoVO.price }}
      </div>
    </div>
  </div>
</template>

<script>
import {OrderApi} from "@/api/api";

export default {
  name: "OrderInfo",
  data() {
    return {
      tableData: [],
      order_code:this.$route.query.order_code
    }
  },
  methods: {
    async init() {
      let data = {
        order_code: this.order_code
      }
      let res = await this.$get2(OrderApi, 0, data)
      if (res.data.code != 1) {
        this.$message.error('服务器异常');
        return
      }
      this.tableData = res.data.data
    }
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>