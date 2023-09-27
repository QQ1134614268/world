const CompressionWebpackPlugin = require('compression-webpack-plugin');
const productionGzipExtensions = ['js', 'css'];
const isProduction = process.env.NODE_ENV === 'production';

module.exports = {
    publicPath: process.env.NODE_ENV === "development" ? "/" : "/",
    // 配置webpack
    configureWebpack: config => {
        config.optimization = {
            runtimeChunk: 'single',
            splitChunks: {
                chunks: 'all',
                maxInitialRequests: Infinity,
                minSize: 20000,
                cacheGroups: {
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name(module) {
                            // get the name. E.g. node_modules/packageName/not/this/part.js
                            // or node_modules/packageName
                            const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1]
                            // npm package names are URL-safe, but some servers don't like @ symbols
                            return `npm.${packageName.replace('@', '')}`
                        }
                    }
                }
            }
        };
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