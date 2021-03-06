const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const clean = require('clean-webpack-plugin');

module.exports = [{
  mode: 'development',
  watch: true,
  entry: './webpack/index.js',
  output: {
    filename: '[name].bundle.js',
    path: path.join(__dirname, 'apps/noobscribe/webs/static/js'),
  },
  devServer: {
    contentBase: path.join(__dirname, 'webpack/dev'),
    compress: true,
    writeToDisk: true,
    port: 9000
  },
  module: {
    rules: [{
      test: /\.css$/,
      use: ['style-loader', 'css-loader']
    }, {
      test: /\.js$/,
      loaders: ['babel-loader']
    }, {
      test: /\.s[ac]ss$/i,
      use: [
        // fallback to style-loader in development
        MiniCssExtractPlugin.loader,
        'css-loader',
        'sass-loader'
      ]
    }, {
      test: /\.(eot|svg|ttf|woff|woff2)$/i,
      loader: "file-loader",
      options: {
        name: '../fonts/[name].[ext]',
      }
    }, {
      test: /\.(png|jpe?g|gif)$/i,
      loader: 'file-loader',
      options: {
        name: '../img/[name].[ext]',
      }
    }]
  },
  plugins: [
    new clean.CleanWebpackPlugin({
      root: path.join(__dirname, 'apps/noobscribe/webs/static'),
      verbose: true
    }),
    new MiniCssExtractPlugin({
      filename: '../css/[name].bundle.css',
      allChunks: true
    })
  ]
}];