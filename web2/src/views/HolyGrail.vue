<template>
  <div class="HolyGrail">
    <header>..header.</header>
    <div class="HolyGrail-body">
      <main class="HolyGrail-content">
        <div>content...1</div>
        <div>content...2</div>
      </main>
      <nav class="HolyGrail-nav">
        <div>nav...1</div>
        <div>nav...2</div>
      </nav>
      <aside class="HolyGrail-ads">...</aside>
    </div>
    <footer>..footer.</footer>
  </div>
</template>

<script>
export default {
  name: "HolyGrail"
}
</script>

<style scoped>

.HolyGrail {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

header,
footer {
  flex: 1;
}

.HolyGrail-body {
  display: flex;
  flex: 1;
}

.HolyGrail-content {
  flex: 1;
}

.HolyGrail-nav, .HolyGrail-ads {
  /* 两个边栏的宽度设为12em */
  flex: 0 0 12em;
}

.HolyGrail-nav {
  /* 导航放到最左边 */
  order: -1;
}


@media (max-width: 768px) {
  .HolyGrail-body {
    flex-direction: column;
    flex: 1;
  }

  .HolyGrail-nav,
  .HolyGrail-ads,
  .HolyGrail-content {
    flex: auto;
  }
}
</style>