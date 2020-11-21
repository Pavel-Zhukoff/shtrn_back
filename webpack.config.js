const path = require('path')

module.exports = {
    entry: {
        index: './app/static/website/js/index.js',
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname,'./app/static/website/js/'),
        publicPath: "/js"
    },
    devServer: {
        overlay: true,
        port: 8000,
    }
}