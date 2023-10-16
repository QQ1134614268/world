<template>
  <div class="p_c_box-flex_center">
    <div id="myChart" style="width: 50rem;height: 30rem"></div>
  </div>
</template>
<!--    <script src="https://cdn.bootcss.com/echarts/5.3.1/echarts.min.js"></script>-->
<script>
export default {
  name: "test_echarts",
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted() {
    this.drawLine();
  },
  methods: {
    async drawLine() {
      await this.init()

      // 基于准备好的dom，初始化echarts实例
      let myChart = echarts.init(document.getElementById('myChart'))
      // 绘制图表
      myChart.setOption({
        title: {text: '在Vue中使用echarts'},
        tooltip: {},
        xAxis: {
          data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }]
      });
    },
    async init() {
      let script = document.createElement("script");  //创建一个script标签
      script.type = "text/javascript";
      script.src = "https://cdn.bootcss.com/echarts/5.3.1/echarts.min.js";
      document.getElementsByTagName('head')[0].appendChild(script);

      await new Promise((resolve) => setTimeout(resolve, 2000));
      // while (echarts === undefined) {
      // }
    }
  },
}
</script>

<style scoped>

</style>