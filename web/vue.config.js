const {defineConfig} = require("@vue/cli-service");
module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: "warning", // eslint 告警级别
    devServer: {
        host: "0.0.0.0",
        port: process.env.PORT,
        open: true,
        hot: true,//浏览器重新刷新
        // hotOnly: false,
        // allowedHosts: "all", // 允许访问的主机列表
        // https: false,
        // historyApiFallback: true, //拦截所有的404,并返回index.html文件（或你指定的其他文件）
        proxy: {
            "^/api/": {
                target: process.env.VUE_APP_BASE_URL,
                changeOrigin: true,
                pathRewrite: { // 路径重写
                    '^/api/': '/api/'
                }
            }
        }
    }
});