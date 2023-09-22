module.exports = {
    publicPath: process.env.NODE_ENV === "development" ? "/" : "/",
    configureWebpack: {
        externals: {
            // vue: 'Vue',
            // 'vue-router': 'VueRouter',
            // axios: 'axios',
            echarts: 'echarts',
        }
    },
    devServer: {
        hot: true,//浏览器重新刷新
        // hotOnly: false,
        open: true,
        host: "0.0.0.0",
        port: process.env.PORT,
        https: false,
        disableHostCheck: true,
        proxy: {
            "/api/": {
                target: process.env.VUE_APP_BASE_URL,
                changeOrigin: true,
                pathRewrite: { // 路径重写
                    '^/api/': '/api/'
                }
            },
            "/upload_file/": {
                target: process.env.NGINX_FILE_SERVER_URL,
                changeOrigin: true,
                pathRewrite: {
                    '^/upload_file/': process.env.NGINX_FILE_SERVER_API
                }
            }
        },
    },
    productionSourceMap: false,
};