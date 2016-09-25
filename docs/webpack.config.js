"use strict";

const ENVIRONMENT = process.env.NODE_ENV || 'development';
const webpack = require('webpack');

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "./bundles/index.js",
  },

  devtool: "source-map",

  plugins: [
    new webpack.DefinePlugin({
      ENVIRONMENT: JSON.stringify(ENVIRONMENT),
    })
  ],

  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel',
        query: {
          presets: ['es2015'],
        },
      },
      {
        test: /\.json$/,
        loader: 'json',
      }
    ],
  }
};
