'use strict'
const pkg = require('../package')

module.exports = {
    port: 4000,
    title: 'ClassGotcha',
    vendor: Object.keys(pkg.dependencies),
    babel: {
        babelrc: false,
        presets: ['vue'],
        plugins: [
            'transform-vue-jsx'
            //   'vue-resource'
        ]
    },
    postcss: [
        require('autoprefixer')({
            // Vue does not support ie 8 and below
            browsers: ['last 2 versions', 'ie > 8']
        }),
        require('postcss-nested')
    ],
    cssModules: true
}
