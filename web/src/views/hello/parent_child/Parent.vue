<!-- 父组件 -->
<template>
  <div class="test">
    <Child @childFn="parentFn"></Child>
    <br/>
    子组件传来的值 : {{ message }}
  </div>
</template>

<script>
import Child from "@/views/hello/parent_child/Child";

export default {
  components: {Child},
  data() {
    return {
      message: ''
    }
  },
  methods: {
    parentFn(payload) {
      this.message = payload;
    }
  }
}
</script>