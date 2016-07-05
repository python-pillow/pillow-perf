AWS Server c4.large
===================

Operations on `RGB` image `2560×1600` pixels on 
Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz

    Test          | Mean time  | Mean perf   | Max perf


Resampling
==========

Pillow 3.2.0
------------
    16x16 bil       0.01968 s   208.13 Mpx/s   208.51 Mpx/s
    16x16 bic       0.03759 s   108.95 Mpx/s   109.10 Mpx/s
    16x16 lzs       0.05876 s    69.70 Mpx/s    69.78 Mpx/s
    320x180 bil     0.02791 s   146.75 Mpx/s   147.43 Mpx/s
    320x180 bic     0.05319 s    77.01 Mpx/s    77.30 Mpx/s
    320x180 lzs     0.08042 s    50.94 Mpx/s    51.04 Mpx/s
    1920x1200 bil   0.09981 s    41.04 Mpx/s    42.26 Mpx/s
    1920x1200 bic   0.13222 s    30.98 Mpx/s    31.36 Mpx/s
    1920x1200 lzs   0.17085 s    23.97 Mpx/s    24.15 Mpx/s
    7712x4352 bil   1.17472 s     3.49 Mpx/s     3.55 Mpx/s
    7712x4352 bic   1.38860 s     2.95 Mpx/s     2.99 Mpx/s
    7712x4352 lzs   1.61358 s     2.54 Mpx/s     2.58 Mpx/s


Pillow 3.3.0
------------
    16x16 bil       0.01201 s   340.91 Mpx/s   343.57 Mpx/s
    16x16 bic       0.02286 s   179.21 Mpx/s   179.60 Mpx/s
    16x16 lzs       0.03743 s   109.43 Mpx/s   109.69 Mpx/s
    320x180 bil     0.01887 s   217.08 Mpx/s   217.84 Mpx/s
    320x180 bic     0.03271 s   125.23 Mpx/s   125.57 Mpx/s
    320x180 lzs     0.05293 s    77.39 Mpx/s    77.45 Mpx/s
    1920x1200 bil   0.07424 s    55.17 Mpx/s    55.34 Mpx/s
    1920x1200 bic   0.09641 s    42.48 Mpx/s    42.54 Mpx/s
    1920x1200 lzs   0.12555 s    32.63 Mpx/s    32.67 Mpx/s
    7712x4352 bil   0.63048 s     6.50 Mpx/s     6.56 Mpx/s
    7712x4352 bic   0.76100 s     5.38 Mpx/s     5.39 Mpx/s
    7712x4352 lzs   0.94698 s     4.33 Mpx/s     4.33 Mpx/s


Pillow-SIMD 3.2.0.post1  SSE4
-----------------------
    16x16 bil       0.01055 s   388.28 Mpx/s   389.47 Mpx/s
    16x16 bic       0.02018 s   203.01 Mpx/s   203.35 Mpx/s
    16x16 lzs       0.03367 s   121.64 Mpx/s   121.81 Mpx/s
    320x180 bil     0.01348 s   303.93 Mpx/s   305.22 Mpx/s
    320x180 bic     0.02540 s   161.28 Mpx/s   161.93 Mpx/s
    320x180 lzs     0.04582 s    89.39 Mpx/s    89.55 Mpx/s
    1920x1200 bil   0.03727 s   109.90 Mpx/s   110.50 Mpx/s
    1920x1200 bic   0.05615 s    72.95 Mpx/s    73.23 Mpx/s
    1920x1200 lzs   0.07891 s    51.91 Mpx/s    52.05 Mpx/s
    7712x4352 bil   0.33490 s    12.23 Mpx/s    12.49 Mpx/s
    7712x4352 bic   0.44974 s     9.11 Mpx/s     9.14 Mpx/s
    7712x4352 lzs   0.58488 s     7.00 Mpx/s     7.01 Mpx/s


Pillow-SIMD 3.3.0.post0  SSE4
-----------------------
    16x16 bil       0.00625 s   655.47 Mpx/s   658.64 Mpx/s
    16x16 bic       0.01196 s   342.45 Mpx/s   344.12 Mpx/s
    16x16 lzs       0.02178 s   188.08 Mpx/s   188.48 Mpx/s
    320x180 bil     0.00810 s   505.81 Mpx/s   510.02 Mpx/s
    320x180 bic     0.01488 s   275.23 Mpx/s   276.03 Mpx/s
    320x180 lzs     0.02684 s   152.59 Mpx/s   153.14 Mpx/s
    1920x1200 bil   0.02632 s   155.65 Mpx/s   156.63 Mpx/s
    1920x1200 bic   0.03947 s   103.78 Mpx/s   104.38 Mpx/s
    1920x1200 lzs   0.05402 s    75.82 Mpx/s    76.40 Mpx/s
    7712x4352 bil   0.22986 s    17.82 Mpx/s    18.35 Mpx/s
    7712x4352 bic   0.29487 s    13.89 Mpx/s    13.91 Mpx/s
    7712x4352 lzs   0.39711 s    10.31 Mpx/s    10.33 Mpx/s


ImageMagick 6.8.9-9
-------------------
    16x16 bil       0.05900 s    69.42 Mpx/s
    16x16 bic       0.10900 s    37.57 Mpx/s
    16x16 lzs       0.16000 s    25.60 Mpx/s
    320x180 bil     0.05900 s    69.42 Mpx/s
    320x180 bic     0.09900 s    41.37 Mpx/s
    320x180 lzs     0.12900 s    31.75 Mpx/s
    1920x1200 bil   0.17900 s    22.88 Mpx/s
    1920x1200 bic   0.23000 s    17.80 Mpx/s
    1920x1200 lzs   0.28900 s    14.17 Mpx/s
    7712x4352 bil   1.21900 s     3.36 Mpx/s
    7712x4352 bic   1.60900 s     2.54 Mpx/s
    7712x4352 lzs   1.94900 s     2.10 Mpx/s


Blur
====

Pillow 3.2.0
------------
    blur 1px        0.22265 s    18.40 Mpx/s    18.46 Mpx/s
    blur 10px       0.22160 s    18.48 Mpx/s    18.57 Mpx/s
    blur 100px      0.22199 s    18.45 Mpx/s    18.50 Mpx/s

Pillow-SIMD 3.2.0.post3  SSE4
-----------------------
    blur 1px        0.09461 s    43.29 Mpx/s    43.69 Mpx/s
    blur 10px       0.09460 s    43.30 Mpx/s    43.58 Mpx/s
    blur 100px      0.09447 s    43.36 Mpx/s    43.59 Mpx/s

ImageMagick 6.8.9-9
-------------------
    blur 1px         0.3290 s    12.45 Mpx/s
    blur 10px        0.9800 s     4.18 Mpx/s
    blur 100px       7.0390 s     0.58 Mpx/s
