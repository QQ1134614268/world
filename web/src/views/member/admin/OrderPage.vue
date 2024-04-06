<template>
  <div class="containerBox">
    <div class="searchBox">
      <el-button size="mini" @click="init">查询</el-button>
    </div>
    <div class="tableBox">
      <el-table :data="page.data">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-table :data="props.row.info_list">
              <el-table-column prop="image" label="图片">
                <template slot-scope="scope">
                  <image :src="scope.row.image" alt="加载失败"></image>
                </template>
              </el-table-column>
              <el-table-column prop="name" label="商品名称"></el-table-column>
              <el-table-column prop="num" label="数量"></el-table-column>
              <el-table-column prop="price" label="单价"></el-table-column>
            </el-table>
          </template>
        </el-table-column>
        <el-table-column prop="user_name" label="用户名"></el-table-column>
        <el-table-column prop="status" label="订单状态"></el-table-column>
        <el-table-column prop="total_price" label="总价"></el-table-column>
        <el-table-column prop="create_time" label="下单时间"></el-table-column>
        <el-table-column label="详情">
          <el-button size="mini" type="danger" @click="info">详情</el-button>
          <el-button size="mini" type="danger" @click="del">删除</el-button>
        </el-table-column>
      </el-table>
    </div>
    <el-pagination @size-change="handleSizeChange"
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
        store_id: this.store_id
      }
      let res = await getJson3(orderPage, data);
      if (res.data.code === 1) {
        this.page = res.data
      } else {
        this.$message.error('服务器异常');
      }
    },
    async info() {
    },
    async del() {
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

    display: flex;
    flex: 0 0 auto;
    align-items: center;
  }
}

</style>
