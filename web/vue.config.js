module.exports = {
    publicPath: process.env.NODE_ENV === "development" ? "/" : "/",
    configureWebpack: {
        externals: {
            vue: 'Vue',
            'vue-router': 'VueRouter',
            axios: 'axios',
            'echarts': 'echarts',

        }
    },
    devServer: {
        open: true,
        host: "0.0.0.0",
        port: process.env.PORT,
        https: false,
        hotOnly: false,
        disableHostCheck: true,
        // proxy: {
        //   "/api": {
        //     target: "", // 本地请求后端真正的地址，只有本地开发时才会做代理，上线不执行这段代码
        //     changeOrigin: true,
        //     pathRewrite: { // 路径重写
        //       "^/api": ""
        //     }
        //   }
        // }
    },
    productionSourceMap: false,
};