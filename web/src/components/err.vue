<template>
  <div style="width: 30%">
    <div>err</div>
    <div style="display: flex; justify-content: space-around">
      <div>注意:</div>
      <div>{{ msg }}</div>
    </div>
    <div style="display: flex; justify-content: space-around">
      <div>data:</div>
      <div>{{ message }}</div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'errComponent',
  props: {
    msg: String
  },
  data() {
    return {
      message: "this is data message"
    }
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
