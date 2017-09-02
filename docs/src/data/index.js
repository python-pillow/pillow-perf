var competitors = {
  "imagemagick-6.8":      {"color": [230, 100, 70], "title": "ImageMagick 6.8.9-9"},
  "opencv-3.1":           {"color": [240, 100, 60], "title": "OpenCV 3.1.0"},
  "skia-53":              {"color": [250, 100, 50], "title": "Skia 53 SSE2"},
  "ipp-2017":             {"color": [250, 100, 30], "title": "IPP 2017 AVX2"},

  "pillow-2.0":           {"color": [10, 90, 50], "title": "PIL & Pillow 2.0 to 2.6"},
  
  "pillow-2.7":           {"color": [340, 90, 43], "title": "Pillow 2.7"},
  "pillow-simd-3.2-sse4": {"color": [340, 90, 75], "title": "Pillow SIMD 3.2.0 SSE4"},
  "pillow-simd-3.2-avx2": {"color": [340, 90, 60], "title": "Pillow SIMD 3.2.0 AVX2"},
  
  "pillow-3.3":           {"color": [190, 90, 43], "title": "Pillow 3.3"},
  "pillow-simd-3.3-sse4": {"color": [190, 90, 75], "title": "Pillow SIMD 3.3.0 SSE4"},
  "pillow-simd-3.3-avx2": {"color": [190, 90, 60], "title": "Pillow SIMD 3.3.0 AVX2"},

  "pillow-3.4":           {"color": [34, 90, 43], "title": "Pillow 3.4.2"},
  "pillow-simd-3.4-sse4": {"color": [34, 90, 75], "title": "Pillow SIMD 3.4.0 SSE4"},
  "pillow-simd-3.4-avx2": {"color": [34, 90, 60], "title": "Pillow SIMD 3.4.0 AVX2"},

  "pillow-4.3":           {"color": [250, 90, 43], "title": "Pillow 4.3-demo"},
  "pillow-simd-4.3-sse4": {"color": [250, 90, 75], "title": "Pillow SIMD 4.3-demo SSE4"},
  "pillow-simd-4.3-avx2": {"color": [250, 90, 60], "title": "Pillow SIMD 4.3-demo AVX2"},
};

var systems = [
  require("./macbook.json"),
  require("./c3.large.json"),
  require("./c4.large.json"),
  require("./amd.a10.7800.json"),
];

module.exports = {
  competitors: competitors,
  systems: systems,
};
