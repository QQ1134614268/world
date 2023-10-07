<template>
  <div>
    <div class="block">
      <router-link :to="{path:'/tree/Catalogue'}" class="p_c_space">
        回到目录
      </router-link>
    </div>
    <div v-for="(item,k) in data" class="p_c_flexbox_row">
      <div class="col-1">{{ item.count }}</div>
      <div>{{ item.name }}</div>
    </div>
  </div>
</template>

<script>
import {ProveBlueprintApi_get_key_word} from "@/api/api";
import {get2} from "@/api/http";

export default {
  name: "KeyWord",
  data() {
    return {
      data: []
    }
  },
  methods: {
    async init() {
      let data = {}
      let res = await get2(ProveBlueprintApi_get_key_word, 0, data)
      if (res.data.code != 1) {
        this.$message.error('服务器异常');
        return
      }
      this.data = res.data.data
    }
  },
  created() {
    this.init()
  },
}
</script>

<style scoped>

</style>