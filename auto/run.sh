#!/bin/bash -e

cd "$(dirname "$0")"

if [ ! -d ~/env/pillow-perf ]; then
  mkdir -p ~/env
  rm -rf ~/env/pillow-perf
  virtualenv ~/env/pillow-perf
  ~/env/pillow-perf/bin/pip install -r ../testsuite/requirements.txt
  ~/env/pillow-perf/bin/pip install opencv-python==3.1.0.5
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
    grep "^version" build.log
  }

  pillow_checkout 2.6.2
  ../../testsuite/run.py scale load convert composition rotate_right "${@:2}"
  
  pillow_checkout 2.7.0
  ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"

  pillow_checkout 3.3.3
  ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"

  pillow_checkout 3.4.2
  ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"

  pillow_checkout v3.2.0.post3 -msse4
  ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"

  if [ "$1" != "no" ]; then
    pillow_checkout v3.2.0.post3 -mavx2
    ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"
  fi

  pillow_checkout v3.3.3.post0 -msse4
  ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"

  if [ "$1" != "no" ]; then
    pillow_checkout v3.3.3.post0 -mavx2
    ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"
  fi

  pillow_checkout v3.4.1.post2 -msse4
  ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"

  if [ "$1" != "no" ]; then
    pillow_checkout v3.4.1.post2 -mavx2
    ../../testsuite/run.py scale load convert blur composition rotate_right "${@:2}"
  fi

  ../../testsuite/run.py wand_scale wand_load wand_convert wand_blur wand_composition wand_rotate_right "${@:2}"

  ../../testsuite/run.py cv2_scale cv2_load cv2_blur cv2_rotate_right "${@:2}"

popd
