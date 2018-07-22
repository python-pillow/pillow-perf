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
        loader: 'json-loader',
      },
      {
        test: require.resolve("./src/index.js"),
        loader: "expose-loader?partialCompetition"
      }
    ],
    noParse: [
      /\/chart.js\/dist\//,
    ]
  }
};
