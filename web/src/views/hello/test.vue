<template>
  <div style="width: 300px;height: 300px" class="p_c_test_border">
    <div style="width: 100px;height: 80%" class="p_c_test_border">
      <img src="@/assets/20181030104146747.jpeg">
    </div>
    <img class="a" src="@/assets/20181030104146747.jpeg" alt="Paris" width="400" height="300">
    <h2>原始图片:</h2>
    <img src="@/assets/20181030104146747.jpeg" alt="Paris" width="400" height="300">
  </div>
</template>

<script>
export default {
  name: "test"
}
</script>

<style scoped>
img, video {
  object-fit: contain;
  max-width: none;
  height: auto;
}

img.a {
  width: 200px;
  height: 400px;
  object-fit: cover;
}
</style>
