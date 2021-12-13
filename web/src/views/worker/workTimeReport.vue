<template>
  <div>
    报表(待确定需求)


  </div>
</template>

<script>
import {WorkTimeAnalyseApi_get_day_report} from "@/api/api";

export default {
  name: "workTimeReport",
  data() {
    return {}
  },
  methods: {
    async init() {
      let data = {
        name: this.name,
        dateType: this.dateType,
        date: this.date,
      }
      let result = await this.$get2(WorkTimeAnalyseApi_get_day_report, 0, data);
      this.data = result.data.data
    },
  },
  created() {
    this.init();
  },
}
</script>

<style scoped>

</style>