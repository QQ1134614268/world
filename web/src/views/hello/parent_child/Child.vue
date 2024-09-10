<!-- 子组件 -->
<template>
  <div class="testCom">
    <input type="text" v-model="message"/>
    <button @click="click">Send</button>
  </div>
</template>
<script>
export default {
  name: 'ChildComponent',
  data() {
    return {
      // 默认
      message: '我是来自子组件的消息'
    }
  },
  methods: {
    click() {
      this.$emit('childFn', this.message);
    }
  }
}
</script>