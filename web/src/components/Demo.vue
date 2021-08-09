<template>
  <div class="txt">
    {{ content }}
  </div>

</template>

<script>

export default {
  name: "Demo",
  methods: {
    onclick() {
      this.$message("ok ....   " + this.url)
    },
  },
  props: {
    url: {
      type: String,
      default: ""
    },
    content: {
      type: String,
      default: "按钮"
    }
  }
}
</script>

<style scoped>
.txt {
  box-sizing: border-box;
  boder: red solid 0.1px;
  /*display block... */
  margin: 0 0 0 0;
  pading: 0 0 0 0;
  wight: auto;
  hight: auto;
  font-size: 16px;
  color: #00D000;
  line-height: 150%;
  background-color: #00D000;
  float: left;


}

</style>