AWS Server c4.large
===================

Operations on `RGB` image `2560×1600` pixels on 
Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz

    Test          | Mean time  | Mean perf   | Max perf


Resampling
==========

Pillow 3.2.0
------------
    16x16 bil       0.01682 s   243.58 Mpx/s   244.04 Mpx/s
    16x16 bic       0.03211 s   127.54 Mpx/s   127.74 Mpx/s
    16x16 lzs       0.04742 s    86.38 Mpx/s    86.43 Mpx/s
    320x180 bil     0.02587 s   158.34 Mpx/s   160.69 Mpx/s
    320x180 bic     0.04606 s    88.93 Mpx/s    89.26 Mpx/s
    320x180 lzs     0.06870 s    59.62 Mpx/s    59.84 Mpx/s
    1920x1200 bil   0.09005 s    45.48 Mpx/s    46.18 Mpx/s
    1920x1200 bic   0.12271 s    33.38 Mpx/s    33.89 Mpx/s
    1920x1200 lzs   0.15257 s    26.85 Mpx/s    27.07 Mpx/s
    7712x4352 bil   1.01583 s     4.03 Mpx/s     4.07 Mpx/s
    7712x4352 bic   1.21211 s     3.38 Mpx/s     3.40 Mpx/s
    7712x4352 lzs   1.42416 s     2.88 Mpx/s     2.90 Mpx/s


Pillow 3.3.0
------------
    16x16 bil       0.01011 s   405.19 Mpx/s   412.78 Mpx/s
    16x16 bic       0.01904 s   215.15 Mpx/s   215.73 Mpx/s
    16x16 lzs       0.02836 s   144.43 Mpx/s   144.62 Mpx/s
    320x180 bil     0.01773 s   231.05 Mpx/s   232.03 Mpx/s
    320x180 bic     0.03072 s   133.33 Mpx/s   133.66 Mpx/s
    320x180 lzs     0.04279 s    95.72 Mpx/s    95.89 Mpx/s
    1920x1200 bil   0.06593 s    62.12 Mpx/s    62.30 Mpx/s
    1920x1200 bic   0.08719 s    46.98 Mpx/s    47.16 Mpx/s
    1920x1200 lzs   0.11192 s    36.60 Mpx/s    36.71 Mpx/s
    7712x4352 bil   0.57514 s     7.12 Mpx/s     7.21 Mpx/s
    7712x4352 bic   0.70128 s     5.84 Mpx/s     5.85 Mpx/s
    7712x4352 lzs   0.85463 s     4.79 Mpx/s     4.80 Mpx/s


Pillow-SIMD 3.2.0.post1
-----------------------

##### SSE4 (default)
    16x16 bil       0.00874 s   468.49 Mpx/s   470.05 Mpx/s
    16x16 bic       0.01650 s   248.23 Mpx/s   248.85 Mpx/s
    16x16 lzs       0.02481 s   165.08 Mpx/s   165.32 Mpx/s
    320x180 bil     0.01260 s   325.20 Mpx/s   326.16 Mpx/s
    320x180 bic     0.02439 s   167.94 Mpx/s   168.46 Mpx/s
    320x180 lzs     0.03870 s   105.84 Mpx/s   106.16 Mpx/s
    1920x1200 bil   0.03245 s   126.21 Mpx/s   127.21 Mpx/s
    1920x1200 bic   0.05018 s    81.62 Mpx/s    82.01 Mpx/s
    1920x1200 lzs   0.06893 s    59.42 Mpx/s    60.10 Mpx/s
    7712x4352 bil   0.29165 s    14.04 Mpx/s    14.37 Mpx/s
    7712x4352 bic   0.40621 s    10.08 Mpx/s    10.10 Mpx/s
    7712x4352 lzs   0.52825 s     7.75 Mpx/s     7.76 Mpx/s

##### AVX2
    16x16 bil       0.00601 s   681.88 Mpx/s   689.90 Mpx/s
    16x16 bic       0.01093 s   374.68 Mpx/s   377.65 Mpx/s
    16x16 lzs       0.01667 s   245.64 Mpx/s   246.60 Mpx/s
    320x180 bil     0.00939 s   435.98 Mpx/s   437.56 Mpx/s
    320x180 bic     0.01754 s   233.55 Mpx/s   235.66 Mpx/s
    320x180 lzs     0.02641 s   155.11 Mpx/s   155.62 Mpx/s
    1920x1200 bil   0.03025 s   135.40 Mpx/s   136.23 Mpx/s
    1920x1200 bic   0.04420 s    92.67 Mpx/s    93.55 Mpx/s
    1920x1200 lzs   0.05893 s    69.50 Mpx/s    69.88 Mpx/s
    7712x4352 bil   0.28285 s    14.48 Mpx/s    14.84 Mpx/s
    7712x4352 bic   0.38850 s    10.54 Mpx/s    10.59 Mpx/s
    7712x4352 lzs   0.49773 s     8.23 Mpx/s     8.24 Mpx/s


Pillow-SIMD 3.3.0.post0
-----------------------

##### SSE4 (default)
    16x16 bil       0.00632 s   648.00 Mpx/s   651.91 Mpx/s
    16x16 bic       0.01175 s   348.72 Mpx/s   349.87 Mpx/s
    16x16 lzs       0.01783 s   229.71 Mpx/s   230.68 Mpx/s
    320x180 bil     0.00833 s   491.54 Mpx/s   495.21 Mpx/s
    320x180 bic     0.01525 s   268.50 Mpx/s   270.24 Mpx/s
    320x180 lzs     0.02317 s   176.79 Mpx/s   177.38 Mpx/s
    1920x1200 bil   0.02699 s   151.77 Mpx/s   152.36 Mpx/s
    1920x1200 bic   0.03937 s   104.03 Mpx/s   104.32 Mpx/s
    1920x1200 lzs   0.04924 s    83.18 Mpx/s    84.04 Mpx/s
    7712x4352 bil   0.23210 s    17.65 Mpx/s    18.18 Mpx/s
    7712x4352 bic   0.30165 s    13.58 Mpx/s    13.60 Mpx/s
    7712x4352 lzs   0.38699 s    10.58 Mpx/s    10.60 Mpx/s

##### AVX2
    16x16 bil       0.00361 s  1134.36 Mpx/s  1143.80 Mpx/s
    16x16 bic       0.00660 s   620.32 Mpx/s   622.50 Mpx/s
    16x16 lzs       0.01072 s   382.12 Mpx/s   392.22 Mpx/s
    320x180 bil     0.00573 s   714.73 Mpx/s   720.12 Mpx/s
    320x180 bic     0.00948 s   432.15 Mpx/s   437.65 Mpx/s
    320x180 lzs     0.01412 s   290.17 Mpx/s   291.72 Mpx/s
    1920x1200 bil   0.02334 s   175.49 Mpx/s   176.76 Mpx/s
    1920x1200 bic   0.03099 s   132.16 Mpx/s   132.62 Mpx/s
    1920x1200 lzs   0.03322 s   123.30 Mpx/s   123.78 Mpx/s
    7712x4352 bil   0.19281 s    21.24 Mpx/s    22.01 Mpx/s
    7712x4352 bic   0.24112 s    16.99 Mpx/s    17.08 Mpx/s
    7712x4352 lzs   0.28983 s    14.13 Mpx/s    14.22 Mpx/s


ImageMagick 6.8.9-9
-------------------
    16x16 bil       0.05900 s  69.4237 Mpx/s
    16x16 bic       0.09900 s  41.3737 Mpx/s
    16x16 lzs       0.16000 s  25.6000 Mpx/s
    320x180 bil     0.05900 s  69.4237 Mpx/s
    320x180 bic     0.08900 s  46.0224 Mpx/s
    320x180 lzs     0.12000 s  34.1333 Mpx/s
    1920x1200 bil   0.17900 s  22.8826 Mpx/s
    1920x1200 bic   0.21900 s  18.7032 Mpx/s
    1920x1200 lzs   0.26900 s  15.2267 Mpx/s
    7712x4352 bil   1.19900 s   3.4161 Mpx/s
    7712x4352 bic   1.53900 s   2.6614 Mpx/s
    7712x4352 lzs   1.82900 s   2.2394 Mpx/s


Blur
====

Pillow 3.2.0
------------
    blur 1px        0.21122 s    19.39 Mpx/s    19.55 Mpx/s
    blur 10px       0.20970 s    19.53 Mpx/s    19.69 Mpx/s
    blur 100px      0.21014 s    19.49 Mpx/s    19.72 Mpx/s

Pillow-SIMD 3.2.0.post3  SSE4
-----------------------
    blur 1px        0.10040 s    40.80 Mpx/s    41.44 Mpx/s
    blur 10px       0.10352 s    39.57 Mpx/s    40.19 Mpx/s
    blur 100px      0.10077 s    40.65 Mpx/s    41.46 Mpx/s

ImageMagick 6.8.9-9
-------------------
    blur 1px         0.3090 s    13.25 Mpx/s
    blur 10px        0.8590 s     4.77 Mpx/s
    blur 100px       6.0800 s     0.67 Mpx/s
