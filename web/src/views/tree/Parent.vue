<template>
  <div>
    <el-input v-model="search">
      <el-button slot="suffix" class="el-icon-search" @click="proveParent(search)">搜索</el-button>
    </el-input>

    <div v-for="(arr,index) in splitRules" :key="index" class="p_c_para">
      <div v-for="(model,index2) in reverse(arr)" class="" :key="index2">
        <span>{{ space.substring(0, index2 * 4) }}</span>
        <span>{{ model.value }}</span>
      </div>

    </div>
  </div>

</template>

<script>
import {ProveBlueprintApi_prove_value_parent} from "@/api/api";
import {get2} from "@/api/http";

export default {
  name: "ParentComponent",
  data() {
    return {
      space: "--------------------------------------------------------------------------------------------",
      search: "",
      splitRules: [],
    }
  },
  methods: {
    reverse(arr) {
      return arr.reverse();
    },
    async proveParent(queryString, callback) {
      let paras = {value: queryString}
      let res = await get2(ProveBlueprintApi_prove_value_parent, 0, paras)
      this.splitRules = res.data.data
    },

    async proveParent2(queryString, callback) {
      let paras = {value: queryString}
      let res = await get2(ProveBlueprintApi_prove_value_parent, 0, paras)
      this.splitRules = []
      let resData = res.data.data

      for (let j = 0; j < resData.length; j++) {
        let arr = resData[j]
        let model = {}
        if (arr.length != 0) {
          model = arr[0]
        }
        let name = ""
        for (let y = 0; y < arr.length; y++) {
          let mo = arr[y]
          name = mo.value + name + " / "
        }
        model.value = name
        this.splitRules.push(model)
      }
    },
  }
}
</script>

<style scoped>

</style>