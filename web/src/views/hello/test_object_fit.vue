<template>
    <div>

        <h1>object-fit 属性</h1>

        <h2>不使用 object-fit:</h2>
        <img src="https://www.runoob.com/try/demo_source/paris.jpg" alt="Paris" style="width:200px;height:400px">

        <h2>object-fit: fill (默认):</h2>
        <img class="fill" src="https://www.runoob.com/try/demo_source/paris.jpg" alt="Paris"
             style="width:200px;height:400px">

        <h2>object-fit: contain:</h2>
        <img class="contain" src="https://www.runoob.com/try/demo_source/paris.jpg" alt="Paris"
             style="width:200px;height:400px">

        <h2>object-fit: cover:</h2>
        <img class="cover" src="https://www.runoob.com/try/demo_source/paris.jpg" alt="Paris"
             style="width:200px;height:400px">

        <h2>object-fit: scale-down:</h2>
        <img class="scale-down" src="https://www.runoob.com/try/demo_source/paris.jpg" alt="Paris"
             style="width:200px;height:400px">

        <h2>object-fit: none:</h2>
        <img class="none" src="https://www.runoob.com/try/demo_source/paris.jpg" alt="Paris"
             style="width:200px;height:400px">

        <p>注意: Internet Explorer/Edge 15 或更早版本的浏览器不支持 object-fit 属性。</p>

    </div>
</template>
<style>
    .fill {
        object-fit: fill;
    }

    .contain {
        object-fit: contain;
    }

    .cover {
        object-fit: cover;
    }

    .scale-down {
        object-fit: scale-down;
    }

    .none {
        object-fit: none;
    }
</style>
