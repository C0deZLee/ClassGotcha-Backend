'use strict'
const webpack = require('webpack')
const base = require('./webpack.base')
const _ = require('./utils')

base.devtool = 'eval-source-map'
base.output.publicPath = '/'
base.plugins.push(
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('development')
    }),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new webpack.LoaderOptionsPlugin({
      debug: true
    })
)

module.exports = base
