#!/bin/bash -e

cd "$(dirname "$0")"

if [ ! -d ~/env/pillow-perf ]; then
  mkdir -p ~/env
  rm -rf ~/env/pillow-perf
  virtualenv ~/env/pillow-perf
  ~/env/pillow-perf/bin/pip install -r ../testsuite/requirements.txt
  ~/env/pillow-perf/bin/pip install opencv-python==3.3.0.10
fi

source ~/env/pillow-perf/bin/activate

git clone https://github.com/uploadcare/pillow-simd.git Pillow || true

pushd Pillow

  git fetch

  function pillow_checkout {
    git checkout -f $1
    touch ./_imaging.c
    CFLAGS="$2" python ./setup.py develop > build.log 2>&1
    grep --color=always "error:" build.log && exit || true
    echo "========================="
    grep "^version" build.log
    echo "========================="
  }

  function MM {
    LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.1 \
    PILLOW_BLOCK_SIZE=128k \
    PILLOW_BLOCKS_MAX=2048 \
    PILLOW_ALIGNMENT=64 \
    "$@"
  }

  pillow_checkout 2.6.2
  ../../testsuite/run.py scale filter -n 5 "${@:2}"
  ../../testsuite/run.py load composition rotate_right "${@:2}"
  
  pillow_checkout 2.7.0
  ../../testsuite/run.py scale blur -n 5 "${@:2}"
  ../../testsuite/run.py convert rotate_right "${@:2}"

  pillow_checkout 3.3.3
  ../../testsuite/run.py scale -n 5 "${@:2}"
  ../../testsuite/run.py convert "${@:2}"

  pillow_checkout 3.4.2
  ../../testsuite/run.py scale -n 5 "${@:2}"
  
  pillow_checkout 4.3.0
  ../../testsuite/run.py scale filter -n 5 "${@:2}"
  ../../testsuite/run.py load convert composition rotate_right "${@:2}"
  MM ../../testsuite/run.py scale filter -n 5 "${@:2}"
  MM ../../testsuite/run.py load convert composition rotate_right "${@:2}"
  

  pillow_checkout v3.2.0.post3 -msse4
  ../../testsuite/run.py scale blur "${@:2}"

  if [ "$1" != "no" ]; then
    pillow_checkout v3.2.0.post3 -mavx2
    ../../testsuite/run.py scale "${@:2}"
  fi

  pillow_checkout v3.3.3.post0 -msse4
  ../../testsuite/run.py scale convert composition "${@:2}"

  if [ "$1" != "no" ]; then
    pillow_checkout v3.3.3.post0 -mavx2
    ../../testsuite/run.py scale convert composition "${@:2}"
  fi

  pillow_checkout v3.4.1.post2 -msse4
  ../../testsuite/run.py scale "${@:2}"

  if [ "$1" != "no" ]; then
    pillow_checkout v3.4.1.post2 -mavx2
    ../../testsuite/run.py scale "${@:2}"
  fi

  pillow_checkout v4.3.0.post0 -msse4
  ../../testsuite/run.py scale convert composition filter "${@:2}"
  MM ../../testsuite/run.py scale convert composition filter "${@:2}"

  if [ "$1" != "no" ]; then
    pillow_checkout v4.3.0.post0 -mavx2
    ../../testsuite/run.py scale convert composition filter "${@:2}"
    MM ../../testsuite/run.py scale convert composition filter "${@:2}"
  fi

  ../../testsuite/run.py wand_scale -n 5 "${@:2}"
  ../../testsuite/run.py wand_blur -n 3 "${@:2}"
  ../../testsuite/run.py wand_load wand_convert wand_composition wand_rotate_right "${@:2}"

  ../../testsuite/run.py cv2_scale cv2_blur -n 5 "${@:2}"
  ../../testsuite/run.py cv2_load cv2_filter cv2_rotate_right "${@:2}"

popd
