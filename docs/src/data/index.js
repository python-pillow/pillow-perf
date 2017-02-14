var colors = {
  "imagemagick-6.7":      [230, 100, 70],
  "imagemagick-6.8":      [230, 100, 70],
  "opencv 2.4.8":         [240, 100, 60],
  "opencv-3.1":           [240, 100, 60],
  "skia-53":              [250, 100, 50],
  "ipp-2017":             [250, 100, 30],

  "pillow-2.0":           [10, 90, 50],
  
  "pillow-2.7":           [340, 90, 43],
  "pillow-simd-3.2-sse4": [340, 90, 75],
  "pillow-simd-3.2-avx2": [340, 90, 60],
  
  "pillow-3.3":           [190, 90, 43],
  "pillow-simd-3.3-sse4": [190, 90, 75],
  "pillow-simd-3.3-avx2": [190, 90, 60],

  "pillow-3.4":           [34, 90, 43],
  "pillow-simd-3.4-sse4": [34, 90, 75],
  "pillow-simd-3.4-avx2": [34, 90, 60],
};

var systems = [
  require("./macbook.json"),
  require("./c3.large.json"),
  require("./c4.large.json"),
  require("./amd.a10.7800.json"),
];

module.exports = {
  colors: colors,
  systems: systems,
};
