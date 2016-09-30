#!/bin/bash

SRC=$1
RUNS=5
IM="convert -bench $RUNS -limit thread 1"
# IM="gm benchmark -iterations $RUNS convert -limit threads 1"
RES="2>&1 | grep '=>/dev/null' | grep -Po '\d+:\K\d+\.\d+' | sort | sed '3!d'"
# RES=""

echo -n "Triangle 16x16  "
eval "$IM -verbose $SRC -filter Triangle -resize 16x16! bmp:/dev/null $RES"
echo -n "Catrom 16x16    "
eval "$IM -verbose $SRC -filter Catrom -resize 16x16! bmp:/dev/null $RES"
echo -n "Lanczos 16x16   "
eval "$IM -verbose $SRC -filter Lanczos -resize 16x16! bmp:/dev/null $RES"

echo -n "Triangle 320x180  "
eval "$IM -verbose $SRC -filter Triangle -resize 320x180! bmp:/dev/null $RES"
echo -n "Catrom 320x180    "
eval "$IM -verbose $SRC -filter Catrom -resize 320x180! bmp:/dev/null $RES"
echo -n "Lanczos 320x180   "
eval "$IM -verbose $SRC -filter Lanczos -resize 320x180! bmp:/dev/null $RES"

echo -n "Triangle 1920x1200  "
eval "$IM -verbose $SRC -filter Triangle -resize 1920x1200! bmp:/dev/null $RES"
echo -n "Catrom 1920x1200    "
eval "$IM -verbose $SRC -filter Catrom -resize 1920x1200! bmp:/dev/null $RES"
echo -n "Lanczos 1920x1200   "
eval "$IM -verbose $SRC -filter Lanczos -resize 1920x1200! bmp:/dev/null $RES"

echo -n "Triangle 7712x4352  "
eval "$IM -verbose $SRC -filter Triangle -resize 7712x4352! bmp:/dev/null $RES"
echo -n "Catrom 7712x4352    "
eval "$IM -verbose $SRC -filter Catrom -resize 7712x4352! bmp:/dev/null $RES"
echo -n "Lanczos 7712x4352   "
eval "$IM -verbose $SRC -filter Lanczos -resize 7712x4352! bmp:/dev/null $RES"

echo -n "Blur 1px    "
eval "$IM -verbose $SRC -blur 2.5x1 bmp:/dev/null $RES"
echo -n "Blur 10px   "
eval "$IM -verbose $SRC -blur 25x10 bmp:/dev/null $RES"
echo -n "Blur 30px   "
eval "$IM -verbose $SRC -blur 75x30 bmp:/dev/null $RES"
