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
        test: /\.css$/,
        loader: "style-loader!css-loader!autoprefixer-loader",
      },
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
