var objectAssign = require('object-assign');

var competitors_meta = {
  "imagemagick-6.8":      {"color": [230, 100, 70], "title": "ImageMagick 6.8.9-9"},
  "opencv-3.1":           {"color": [240, 100, 60], "title": "OpenCV 3.1.0"},
  "opencv-3.3":           {"color": [240, 100, 60], "title": "OpenCV 3.3.0"},
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

  "pillow-4.3":           {"color": [210, 90, 43], "title": "Pillow 4.3.0"},
  "pillow-simd-4.3-sse4": {"color": [210, 90, 75], "title": "Pillow SIMD 4.3.0 SSE4"},
  "pillow-simd-4.3-avx2": {"color": [210, 90, 60], "title": "Pillow SIMD 4.3.0 AVX2"},
};

var competitions_meta = {
  "resample-4k-rgb" : {
    "topic": "resampling",
    "title": "Resize 2560x1600 RGB image",
    "preposition": " to",
    "source": {"size": [2560, 1600]},
    "columns": [
      {"name": "resolution", "title": "Destination resolution"},
      {
        "name": "filter",
        "title": "Convolution filter",
        "map": {
          "bil": "Bilinear",
          "bic": "Bicubic",
          "lzs": "Lanczos"
        }
      },
      {"name": "result", "units": "s"}
    ],
  },
  "image-io-4k-rgb": {
    "title": "Input/Output 2560×1600 RGB image",
    "preposition": ".",
    "source": {"size": [2560, 1600]},
    "columns": [
      {"name": "operation", "title": "Operation"},
      {"name": "result", "units": "s"}
    ],
  },
  "blur-4k-rgb": {
    "topic": "blur",
    "title": "Blur 2560×1600 RGB image",
    "preposition": ",",
    "source": {"size": [2560, 1600]},
    "columns": [
      {"name": "radius", "title": "Blur radius"},
      {"name": "result", "units": "s"}
    ],
  },
  "filter-4k-rgb": {
    "title": "Kernel filter 2560×1600 RGB image",
    "preposition": ".",
    "source": {"size": [2560, 1600]},
    "columns": [
        {"name": "kernel", "title": "Kernel"},
        {"name": "result","units": "s"}
    ],
  },
  "transposition-4k-rgb": {
    "topic": "transposition",
    "title": "Transpose 2560×1600 RGB image",
    "preposition": ".",
    "source": {"size": [2560, 1600]},
    "columns": [
      {"name": "operation", "title": "Operation"},
      {"name": "result", "units": "s"}
    ],
  },
  "conversion-4k-rgb": {
    "topic": "conversion",
    "title": "Color conversion 2560×1600 image",
    "preposition": ".",
    "source": {"size": [2560, 1600]},
    "columns": [
      {"name": "modes", "title": "Modes"},
      {"name": "result", "units": "s"}
    ],
  },
  "composition-4k-rgb": {
		"topic": "compositing",
    "title": "Composition two 2560×1600 RGBA images",
    "preposition": ".",
    "source": {"size": [2560, 1600]},
    "columns": [
      {"name": "radius", "title": "Blur radius"},
      {"name": "result", "units": "s"}
    ],
  },
};


function fillSystemWithMeta(system) {
  var i, j;
  system = objectAssign({}, system);

  for (j = 0; j < system.competitions.length; j++) {
  	var competition = system.competitions[j];
  	system.competitions[j] = competition = objectAssign(
  		{}, competitions_meta[competition.name], competition);

  	for (i = 0; i < competition.competitors.length; i++) {
  		var competitor = competition.competitors[i];
  		competition.competitors[i] = competitor = objectAssign(
  			{}, competitors_meta[competitor.name], competitor);
  	}
  }
  return system;
}

module.exports = {
  systems: [
	  fillSystemWithMeta(require("./macbook.json")),
	  fillSystemWithMeta(require("./c3.large.json")),
	  fillSystemWithMeta(require("./c4.large.json")),
	  fillSystemWithMeta(require("./amd.a10.7800.json")),
	],
};
