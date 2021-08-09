<template>
  <div>
    {{ url }}
  </div>
</template>

<script>
export default {
  name: "ButtonComponent",
  props: {
    url: {
      type: String,
      default: ""
    },
  }

}
</script>

<style scoped>

</style>