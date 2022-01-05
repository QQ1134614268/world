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
        proxy: { //todo /upload/xxx.png
            "/api": {
                target: process.env.VUE_APP_BASE_URL,
                changeOrigin: true,
                pathRewrite: { // 路径重写
                    '^/api': '/api'
                }
            }
        }
    },
    productionSourceMap: false,
};