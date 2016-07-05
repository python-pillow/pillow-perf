Macbook Pro late 2013
=====================

Operations on `RGB` image `2560×1600` pixels on 
Intel(R) Core(TM) i5-4258U CPU @ 2.40GHz

    Test          | Mean time  | Mean perf   | Max perf


Resampling
==========

Pillow 3.2.0
------------
    16x16 bil       0.02031 s   201.70 Mpx/s   216.37 Mpx/s
    16x16 bic       0.03882 s   105.53 Mpx/s   111.29 Mpx/s
    16x16 lzs       0.05547 s    73.84 Mpx/s    75.40 Mpx/s
    320x180 bil     0.03052 s   134.19 Mpx/s   142.97 Mpx/s
    320x180 bic     0.05457 s    75.06 Mpx/s    78.74 Mpx/s
    320x180 lzs     0.07996 s    51.23 Mpx/s    52.34 Mpx/s
    1920x1200 bil   0.11725 s    34.94 Mpx/s    35.68 Mpx/s
    1920x1200 bic   0.14903 s    27.48 Mpx/s    27.89 Mpx/s
    1920x1200 lzs   0.17944 s    22.83 Mpx/s    23.29 Mpx/s
    7712x4352 bil   0.91945 s     4.45 Mpx/s     4.49 Mpx/s
    7712x4352 bic   1.12454 s     3.64 Mpx/s     3.68 Mpx/s
    7712x4352 lzs   1.33199 s     3.08 Mpx/s     3.10 Mpx/s


Pillow 3.3.0
------------
    16x16 bil       0.01215 s   337.12 Mpx/s   363.19 Mpx/s
    16x16 bic       0.02205 s   185.79 Mpx/s   193.76 Mpx/s
    16x16 lzs       0.03616 s   113.27 Mpx/s   129.33 Mpx/s
    320x180 bil     0.01959 s   209.06 Mpx/s   220.60 Mpx/s
    320x180 bic     0.03292 s   124.43 Mpx/s   129.79 Mpx/s
    320x180 lzs     0.04980 s    82.25 Mpx/s    85.54 Mpx/s
    1920x1200 bil   0.07332 s    55.87 Mpx/s    56.57 Mpx/s
    1920x1200 bic   0.09387 s    43.64 Mpx/s    44.09 Mpx/s
    1920x1200 lzs   0.11868 s    34.51 Mpx/s    35.15 Mpx/s
    7712x4352 bil   0.61001 s     6.71 Mpx/s     6.75 Mpx/s
    7712x4352 bic   0.74344 s     5.51 Mpx/s     5.61 Mpx/s
    7712x4352 lzs   0.88627 s     4.62 Mpx/s     4.67 Mpx/s


Pillow 3.4.0, preliminary
------------
    16x16 bil       0.01196 s   342.59 Mpx/s   367.59 Mpx/s
    16x16 bic       0.02276 s   179.97 Mpx/s   193.45 Mpx/s
    16x16 lzs       0.03324 s   123.23 Mpx/s   128.26 Mpx/s
    320x180 bil     0.01909 s   214.59 Mpx/s   224.82 Mpx/s
    320x180 bic     0.03161 s   129.58 Mpx/s   137.27 Mpx/s
    320x180 lzs     0.04811 s    85.14 Mpx/s    89.21 Mpx/s
    1920x1200 bil   0.05610 s    73.01 Mpx/s    75.10 Mpx/s
    1920x1200 bic   0.07734 s    52.96 Mpx/s    54.37 Mpx/s
    1920x1200 lzs   0.10153 s    40.34 Mpx/s    40.80 Mpx/s
    7712x4352 bil   0.46097 s     8.89 Mpx/s     9.00 Mpx/s
    7712x4352 bic   0.58970 s     6.95 Mpx/s     7.09 Mpx/s
    7712x4352 lzs   0.74292 s     5.51 Mpx/s     5.64 Mpx/s


Pillow-SIMD 3.2.0.post1
-----------------------

##### SSE4 (default)
    16x16 bil       0.00960 s   426.84 Mpx/s   456.98 Mpx/s
    16x16 bic       0.01844 s   222.14 Mpx/s   241.49 Mpx/s
    16x16 lzs       0.02802 s   146.17 Mpx/s   157.77 Mpx/s
    320x180 bil     0.01378 s   297.31 Mpx/s   323.31 Mpx/s
    320x180 bic     0.02464 s   166.21 Mpx/s   177.58 Mpx/s
    320x180 lzs     0.03809 s   107.55 Mpx/s   113.83 Mpx/s
    1920x1200 bil   0.03880 s   105.57 Mpx/s   109.35 Mpx/s
    1920x1200 bic   0.05805 s    70.56 Mpx/s    73.04 Mpx/s
    1920x1200 lzs   0.07547 s    54.28 Mpx/s    55.51 Mpx/s
    7712x4352 bil   0.31640 s    12.95 Mpx/s    13.17 Mpx/s
    7712x4352 bic   0.43977 s     9.31 Mpx/s     9.45 Mpx/s
    7712x4352 lzs   0.57375 s     7.14 Mpx/s     7.28 Mpx/s

##### AVX2
    16x16 bil       0.00846 s   484.04 Mpx/s   546.35 Mpx/s
    16x16 bic       0.01475 s   277.71 Mpx/s   291.41 Mpx/s
    16x16 lzs       0.02314 s   177.05 Mpx/s   190.64 Mpx/s
    320x180 bil     0.01296 s   315.97 Mpx/s   354.51 Mpx/s
    320x180 bic     0.02210 s   185.33 Mpx/s   197.28 Mpx/s
    320x180 lzs     0.03311 s   123.69 Mpx/s   129.94 Mpx/s
    1920x1200 bil   0.03823 s   107.13 Mpx/s   114.87 Mpx/s
    1920x1200 bic   0.05332 s    76.81 Mpx/s    81.82 Mpx/s
    1920x1200 lzs   0.06656 s    61.54 Mpx/s    62.83 Mpx/s
    7712x4352 bil   0.30947 s    13.24 Mpx/s    13.41 Mpx/s
    7712x4352 bic   0.43915 s     9.33 Mpx/s    10.15 Mpx/s
    7712x4352 lzs   0.52902 s     7.74 Mpx/s     8.10 Mpx/s


Pillow-SIMD 3.3.0.post0
-----------------------

##### SSE4 (default)
    16x16 bil       0.00716 s   571.67 Mpx/s   581.58 Mpx/s
    16x16 bic       0.01340 s   305.72 Mpx/s   318.85 Mpx/s
    16x16 lzs       0.02165 s   189.19 Mpx/s   210.58 Mpx/s
    320x180 bil     0.01118 s   366.33 Mpx/s   422.70 Mpx/s
    320x180 bic     0.01821 s   224.91 Mpx/s   237.04 Mpx/s
    320x180 lzs     0.02675 s   153.10 Mpx/s   158.98 Mpx/s
    1920x1200 bil   0.03120 s   131.27 Mpx/s   140.47 Mpx/s
    1920x1200 bic   0.04541 s    90.20 Mpx/s    94.55 Mpx/s
    1920x1200 lzs   0.05646 s    72.55 Mpx/s    74.08 Mpx/s
    7712x4352 bil   0.25503 s    16.06 Mpx/s    16.26 Mpx/s
    7712x4352 bic   0.32377 s    12.65 Mpx/s    13.15 Mpx/s
    7712x4352 lzs   0.41647 s     9.84 Mpx/s    10.10 Mpx/s

##### AVX2
    16x16 bil       0.00453 s   903.40 Mpx/s   934.09 Mpx/s
    16x16 bic       0.00741 s   552.85 Mpx/s   570.08 Mpx/s
    16x16 lzs       0.01153 s   355.40 Mpx/s   366.73 Mpx/s
    320x180 bil     0.00733 s   558.57 Mpx/s   580.01 Mpx/s
    320x180 bic     0.01159 s   353.53 Mpx/s   366.70 Mpx/s
    320x180 lzs     0.01677 s   244.22 Mpx/s   252.67 Mpx/s
    1920x1200 bil   0.02693 s   152.11 Mpx/s   159.79 Mpx/s
    1920x1200 bic   0.03646 s   112.34 Mpx/s   116.78 Mpx/s
    1920x1200 lzs   0.03971 s   103.16 Mpx/s   108.57 Mpx/s
    7712x4352 bil   0.20146 s    20.33 Mpx/s    21.23 Mpx/s
    7712x4352 bic   0.24879 s    16.46 Mpx/s    17.10 Mpx/s
    7712x4352 lzs   0.30612 s    13.38 Mpx/s    13.92 Mpx/s


Pillow-SIMD 3.4.0.post0, preliminary
-----------------------

##### SSE4 (default)
    16x16 bil       0.00319 s  1282.85 Mpx/s  1309.84 Mpx/s
    16x16 bic       0.00575 s   712.95 Mpx/s   716.57 Mpx/s
    16x16 lzs       0.00934 s   438.60 Mpx/s   442.77 Mpx/s
    320x180 bil     0.00474 s   863.40 Mpx/s   882.74 Mpx/s
    320x180 bic     0.00813 s   503.75 Mpx/s   512.25 Mpx/s
    320x180 lzs     0.01313 s   312.05 Mpx/s   324.98 Mpx/s
    1920x1200 bil   0.01904 s   215.15 Mpx/s   228.44 Mpx/s
    1920x1200 bic   0.02404 s   170.41 Mpx/s   177.40 Mpx/s
    1920x1200 lzs   0.03151 s   130.00 Mpx/s   136.62 Mpx/s
    7712x4352 bil   0.17956 s    22.81 Mpx/s    23.88 Mpx/s
    7712x4352 bic   0.22463 s    18.23 Mpx/s    19.21 Mpx/s
    7712x4352 lzs   0.27496 s    14.90 Mpx/s    15.62 Mpx/s

##### AVX2
    16x16 bil       0.00256 s  1601.85 Mpx/s  1666.49 Mpx/s
    16x16 bic       0.00455 s   900.65 Mpx/s   920.43 Mpx/s
    16x16 lzs       0.00752 s   544.89 Mpx/s   549.79 Mpx/s
    320x180 bil     0.00387 s  1057.81 Mpx/s  1086.51 Mpx/s
    320x180 bic     0.00811 s   504.76 Mpx/s   642.62 Mpx/s
    320x180 lzs     0.01064 s   384.92 Mpx/s   410.01 Mpx/s
    1920x1200 bil   0.01527 s   268.29 Mpx/s   293.12 Mpx/s
    1920x1200 bic   0.01945 s   210.62 Mpx/s   217.40 Mpx/s
    1920x1200 lzs   0.02520 s   162.57 Mpx/s   178.76 Mpx/s
    7712x4352 bil   0.14041 s    29.17 Mpx/s    31.86 Mpx/s
    7712x4352 bic   0.17111 s    23.94 Mpx/s    24.81 Mpx/s
    7712x4352 lzs   0.20077 s    20.40 Mpx/s    20.98 Mpx/s


Skia 53
-------
    16x16 bil       0.00506 s   809.49 Mpx/s   815.94 Mpx/s
    16x16 bic       0.00904 s   453.10 Mpx/s   470.26 Mpx/s
    16x16 lzs       0.01400 s   292.57 Mpx/s   310.30 Mpx/s
    320x180 bil     0.00691 s   592.76 Mpx/s   615.02 Mpx/s
    320x180 bic     0.01250 s   327.68 Mpx/s   338.51 Mpx/s
    320x180 lzs     0.02080 s   196.92 Mpx/s   211.13 Mpx/s
    1920x1200 bil   0.02130 s   192.30 Mpx/s   196.92 Mpx/s
    1920x1200 bic   0.03630 s   112.84 Mpx/s   119.77 Mpx/s
    1920x1200 lzs   0.03910 s   104.76 Mpx/s   106.67 Mpx/s
    7712x4352 bil   0.19900 s    20.58 Mpx/s    21.11 Mpx/s
    7712x4352 bic   0.24800 s    16.52 Mpx/s    17.07 Mpx/s
    7712x4352 lzs   0.34000 s    12.05 Mpx/s    12.45 Mpx/s


ImageMagick 6.8.9-9
-------------------
    16x16 bil       0.09900 s    41.37 Mpx/s
    16x16 bic       0.19900 s    20.58 Mpx/s
    16x16 lzs       0.28900 s    14.17 Mpx/s
    320x180 bil     0.13900 s    29.46 Mpx/s
    320x180 bic     0.26000 s    15.75 Mpx/s
    320x180 lzs     0.37900 s    10.80 Mpx/s
    1920x1200 bil   0.23000 s    17.80 Mpx/s
    1920x1200 bic   0.41000 s     9.99 Mpx/s
    1920x1200 lzs   0.58900 s     6.95 Mpx/s
    7712x4352 bil   1.60900 s     2.54 Mpx/s
    7712x4352 bic   2.55000 s     1.60 Mpx/s
    7712x4352 lzs   3.75000 s     1.09 Mpx/s


Blur
====

Pillow 3.2.0
------------
    blur 1px        0.24177 s    16.94 Mpx/s    17.18 Mpx/s
    blur 10px       0.24173 s    16.94 Mpx/s    17.23 Mpx/s
    blur 100px      0.24188 s    16.93 Mpx/s    17.25 Mpx/s

Pillow-SIMD 3.2.0.post3  SSE4
-----------------------
    blur 1px        0.11649 s    35.16 Mpx/s    35.96 Mpx/s
    blur 10px       0.11549 s    35.47 Mpx/s    36.19 Mpx/s
    blur 100px      0.11527 s    35.53 Mpx/s    36.27 Mpx/s

ImageMagick 6.8.9-9
-------------------
    blur 1px         0.6200 s     6.60 Mpx/s
    blur 10px        1.7900 s     2.28 Mpx/s
    blur 100px      12.0090 s     0.34 Mpx/s
