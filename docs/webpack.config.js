"use strict";

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "./bundles/index.js",
  },

  devtool: "source-map",

  module: {
    loaders: [
      {
        test: /\.json$/,
        loader: 'json',
      }
    ],
    noParse: [
      /\/chart.js\/dist\//,
    ]
  }
};
