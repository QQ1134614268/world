<template>
  <div>

    <div style="margin:0 auto;width: 100%;">
      <div>
        <div v-for="item in workerUrls ">
          <a :href=item.url>{{ item.name }}</a>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "UserSpace",

  data() {
    return {
      workerUrls: [
        {url: "/worker/Worker", name: "工人列表"},
        {url: "/worker/MonthTime3", name: "每日打卡"},
        {url: "/worker/MonthTime2", name: "批量打卡"},
        {url: "/worker/WorkerTime", name: "每日考勤"},
        {url: "/worker/MonthTime", name: "月度考勤"},
      ],
    };
  },
  methods: {},
  created() {
  }
}
</script>

<style scoped>

</style>
