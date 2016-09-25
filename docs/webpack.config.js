"use strict";

const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "./bundles/index.js",
  },
  devtool: "source-map",
};