<template>
  <div class="containerBox">
    <!--        订单(搜索) (商家, 后台, 用户)-->
    <div class="searchBox">
      <el-button @click="init">查询</el-button>
    </div>
    <div class="tableBox">
      <div v-for="(item,index) in page.data" class="orderBox">
        <div class="order">
          <span>{{ item.create_time }}</span>
          <span>{{ item.total_price }}</span>
        </div>
        <div v-for="(item1,index2) in item.info_list" class="orderInfo">
          <span class="food">
            <img :src="item1.image" style="width: 3rem;">
            <span>{{ item1.name }}</span>
          </span>
          <span>{{ item1.price }}</span>
          <span>x{{ item1.num }}</span>
        </div>
      </div>
    </div>
    <el-pagination v-if="page.total" @size-change="handleSizeChange"
                   @current-change="handleCurrentChange"
                   :current-page="page.page"
                   :page-size="page.page_size"
                   :total="page.total"
                   layout=" prev, pager, next, total">
    </el-pagination>
  </div>
</template>

<script>
import {orderPage} from "@/api/api";
import {getJson3} from "@/api/http";

export default {
  name: "GoodsAdd",
  data() {
    return {
      store_id: null,
      user_id: null,
      page: {
        page: 1,
        page_size: 10,
        data: [],
      },
    }
  },
  methods: {
    async init() {
      let data = {
        currentPage: this.page.page,
        pageSize: this.page.page_size,
        store_id: this.store_id,
        user_id: this.user_id,
      }
      let res = await getJson3(orderPage, data);
      if (res.data.code === 1) {
        this.page = res.data
      } else {
        this.$message.error('服务器异常');
      }
    },
    handleCurrentChange(val) {
      this.page.page = val;
      this.init();
    },
    handleSizeChange(val) {
      this.page.page_size = val;
      this.init();
    },
  },
  created() {
    this.init()
  }
}
</script>

<style scoped lang="less">
.containerBox {
  width: 100%;
  padding: 1rem;

  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  //justify-content: center;
  align-items: center;

  .searchBox {
    width: 100%;
    height: 3rem;

    //margin-top: 1rem;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);

    background-color: #ffffff;
    border-radius: 0.75rem;

    display: flex;
    flex: 0 0 auto;
    align-items: center;
  }

  .actionBox {
    width: 100%;
    height: 3rem;

    //margin-top: 1rem;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);

    background-color: #ffffff;
    border-radius: 0.75rem;

    display: flex;
    flex: 0 0 auto;
    align-items: center;
  }

  .tableBox {
    width: 100%;
    //margin-top: 1rem;
    box-shadow: 0 0.2rem 1rem 0 rgba(0, 0, 0, 0.15);

    background-color: #ffffff;
    border-radius: 0.75rem;

    .orderBox {
      margin: 1rem;
      border: black solid 1px;

      .order {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 0.4rem;
      }

      .orderInfo {
        .food {
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
    }
  }
}

</style>
