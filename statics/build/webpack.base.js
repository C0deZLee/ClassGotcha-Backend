'use strict'
const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const config = require('./config')
const _ = require('./utils')

module.exports = {
  entry: {
    client: './client/index.js'
  },
  output: {
    path: _.outputPath,
    filename: '[name].js',
    publicPath: './'
  },
  resolve: {
    extensions: ['', '.js', '.vue', '.css', '.json'],
    alias: {
      root: path.join(__dirname, '../client'),
      components: path.join(__dirname, '../client/components'),
      patterns: path.join(__dirname, '../client/css/patterns'),
      css: path.join(__dirname, '../client/css'),
      img: path.join(__dirname, '../client/img')
    }
  },
  module: {
    loaders: [{
      test: /\.vue$/,
      loaders: ['vue']
    }, {
      test: /\.js$/,
      loaders: ['babel'],
      exclude: [/node_modules/]
    }, {
      test: /\.es6$/,
      loaders: ['babel']
    }, {
      test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
      loader: 'url',
      query: {
        limit: 10000,
        name: 'static/img/[name].[hash:7].[ext]'
      }
    }, {
      test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
      loader: 'url',
      query: {
        limit: 10000,
        name: 'static/fonts/[name].[hash:7].[ext]'
      }
    }]
  },
  babel: config.babel,
  postcss: config.postcss,
  vue: {
    loaders: {
      scss: 'style!css!sass',
      sass: 'style!css!sass'
    },
    postcss: config.postcss
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: config.title,
      template: path.join(__dirname, '/index.html'),
      filename: _.outputIndexPath
    })
  ],
  target: _.target
}