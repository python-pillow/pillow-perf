"use strict";

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "index.js",
    path: __dirname + "/bundles/",
  },

  devtool: "source-map",
  mode: "development",

  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          {
            loader: 'postcss-loader',
            options: {
              plugins: [
                require('autoprefixer'),
              ]
            }
          },
        ]
      },
      {
        test: require.resolve("./src/index.js"),
        use: {
          loader: "expose-loader",
          options: "partialCompetition",
        }
      }
    ],
    noParse: [
      /\/chart.js\/dist\//,
    ]
  }
};
