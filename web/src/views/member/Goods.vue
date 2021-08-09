<template>
  <div style="display: flex;">
    <div style="width: 20rem">
      <div>
        <el-button @click="showCtl('a')"> 商品列表</el-button>
      </div>
      <div>
        <el-button @click="showCtl('c')"> 购买列表</el-button>
      </div>
      <div>
        <el-button @click="showCtl('d')"> 订单列表</el-button>
      </div>
      <div>
        <el-button @click="showCtl('b')"> 添加商品</el-button>
      </div>
      <div>
        <!--        todo-->
        <a href=""> 上一级 </a>
      </div>
    </div>
    <div style="width: 100rem">
      <div><span style="color: blue">{{ store.name }}</span>店铺</div>
      <div v-if="ctl.a">
        <el-table :data="tableData" style="width: 100%">
          <el-table-column prop="name" label="商品名" width="180"></el-table-column>
          <el-table-column prop="price" label="商品价格"></el-table-column>
          <el-table-column prop="describe" label="商品描述"></el-table-column>
          <el-table-column prop="create_time" label="上架时间"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div v-if="ctl.c">
        <div>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="name" label="商品名" width="180"></el-table-column>
            <el-table-column prop="price" label="商品价格"></el-table-column>
            <el-table-column prop="describe" label="商品描述"></el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-input-number v-model="scope.row.num" @change="add(scope.row)" :min="0"
                                 label="添加"></el-input-number>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <div>
          <el-table :data="chart" style="width: 100%">
            <el-table-column prop="name" label="商品名" width="180"></el-table-column>
            <el-table-column prop="price" label="商品价格"></el-table-column>
            <el-table-column label="数量">
              <template slot-scope="scope">
                <el-input-number v-model="scope.row.num" :min="0" label="添加"></el-input-number>
              </template>
            </el-table-column>
          </el-table>
          <el-button @click="buy"> 结算</el-button>
        </div>
      </div>
      <div v-if="ctl.d">
        <el-table :data="order_list" style="width: 100%">
          <el-table-column prop="name" label="商品名" width="180"></el-table-column>
          <el-table-column prop="num" label="数量" width="180"></el-table-column>
        </el-table>
      </div>
      <div v-if="ctl.b">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="商品名">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="商品价格">
            <el-input v-model="form.price" :value="null"></el-input>
          </el-form-item>
          <el-form-item label="商品描述">
            <el-input v-model="form.describe"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">完成</el-button>
            <el-button @click="cancel">取消</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Goods",
  data() {
    return {
      order_list: [],
      chart: [],
      num: "",
      store_id: this.$route.query.store_id,
      form: {
        name: '',
        describe: '',
        price: '',
      },
      store: {
        name: 111
      },
      ctl: {
        a: true
      },
      tableData: []
    };
  },
  methods: {
    async buy() {
      let url = "/api/member/OrderApi"
      let response = await this.$postJson(url, this.chart);
      if (response.data.code != 1) {
        alert("2")
        return
      }
      this.store = response.data.data
    },
    async getOrderList() {
      let url = "/api/member/OrderListApi"
      let response = await this.$get(url);
      if (response.data.code != 1) {
        alert("2")
        return
      }
      this.order_list = response.data.data
    },
    add(row) {
      this.chart = this.tableData.filter(function (item) {
        if (item.num != undefined && item.num != 0) {
          return item;
        }
      });
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {
          });
    },
    showCtl(arg = "a") {
      this.ctl = {}
      this.ctl[arg] = true
    },
    async getStoreById(id) {
      //todo
      let url = "/api/member/StoreApi"
      let data = {
        id: this.$route.query.id
      }
      let response = await this.$get(url, data);
      if (response.data.code != 1) {
        alert("2")
        return
      }
      this.store = response.data.data
    },
    async getGoodsList() {
      let url = "api/goods_list"
      let data = {
        store_id: this.store_id,
      }
      let response = await this.$get(url, data);
      if (response.data.code != 1) {
        alert("2")
        return
      }
      this.tableData = response.data.data
    },
    async handleEdit(index, row) {
      this.showCtl('b')
      this.form = row
    },
    async handleDelete(index, row) {
      let url = "api/goods" + "/" + row.id
      let response = await this.$deleteJson(url);
      if (response.data.code != 1) {
        return
      }
      this.tableData.splice(index, 1)
    },
    async onSubmit() {
      let url = "api/goods"
      this.form.store_id = this.store_id
      let response = await this.$ppJson(url, this.form, this.form.id);
      if (response.data.code != 1) {
        this.$message('操作失败');
      } else {
        this.$message('操作成功');
      }
      await this.getGoodsList()
      this.showCtl("a")
      this.form = {}
    },
    cancel() {

    }
  },
  created() {
    this.getGoodsList()
    this.getOrderList()

  }
}
</script>

<style scoped>

</style>