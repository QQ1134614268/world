<template>
  <div>
    店内钱包-- 网吧 todo
    接入三方支付
    <div v-for="(item,k) in memberList" style="display: flex">
      <div>{{ item.user_id }}</div>
      <div>
        <el-button type="success" @click="getWallet(item)">获取余额</el-button>
        <div v-if="item.wallet">余额:{{ item.wallet.money }}</div>
      </div>
      <div style="display: flex">
        <input v-model.number="addMoneyNum"></input>
        <el-button type="success" @click="addMoney(item)">充值</el-button>
      </div>
      <div style="display: flex">
        <input v-model.number="payMoneyNum"></input>
        <el-button type="success" @click="payMoney(item)">消费</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import {WalletApi} from "@/api/api";
import {get2, putJson2} from "@/api/http";

export default {
  name: "Wallet",
  data() {
    return {
      store_id: this.$route.query.id,
      memberList: "",
      addMoneyNum: "",
      payMoneyNum: "",
    };
  },
  methods: {
    async getWallet(item) {
      let data = {
        id: item.id
      }
      let response = await get2(WalletApi,data.id, data);
      if (response.data.code != 1) {
        return
      }
      this.$set(item, "wallet", response.data.data)
    },
    async addMoney(item) {
      let data = {
        id: item.id,
        money: this.addMoneyNum,
      }
      let response = await putJson2(WalletApi,data.id, data);
      if (response.data.code != 1) {
        return
      }
      item["money"] = response.data.data
    },
    async payMoney(item) {
      let data = {
        id: item.id,
        money: -this.payMoneyNum,
      }
      let response = await putJson2(WalletApi,data.id, data);
      if (response.data.code != 1) {
        return
      }
      item["money"] = response.data.data
    },
  }
}
</script>

<style scoped>

</style>