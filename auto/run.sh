#!/bin/bash -e

cd "$(dirname "$0")"

if [ ! -d ~/env/pillow-perf ]; then
  mkdir -p ~/env
  rm -rf ~/env/pillow-perf
  virtualenv ~/env/pillow-perf
  ~/env/pillow-perf/bin/pip install -r ../testsuite/requirements.txt
fi

source ~/env/pillow-perf/bin/activate

git clone https://github.com/uploadcare/pillow-simd.git Pillow || true

pushd Pillow

  git fetch

  function checkout {
    git checkout -f $1
    touch ./_imaging.c
    CFLAGS="$2" python ./setup.py develop > build.log 2>&1
    grep --color=always "error:" build.log && exit || true
    grep "^version" build.log
  }

  checkout 2.6.2
  ../../testsuite/run.py scale "${@:2}"
  
  checkout 2.7.0
  ../../testsuite/run.py scale "${@:2}"

  checkout 3.3.3
  ../../testsuite/run.py scale "${@:2}"

  checkout 3.4.1
  ../../testsuite/run.py scale "${@:2}"

  checkout v3.2.0.post3 -msse4
  ../../testsuite/run.py scale "${@:2}"

  if [ "$1" != "no" ]; then
    checkout v3.2.0.post3 -mavx2
    ../../testsuite/run.py scale "${@:2}"
  fi

  checkout v3.3.3.post0 -msse4
  ../../testsuite/run.py scale "${@:2}"

  if [ "$1" != "no" ]; then
    checkout v3.3.3.post0 -mavx2
    ../../testsuite/run.py scale "${@:2}"
  fi

  checkout v3.4.1.post1 -msse4
  ../../testsuite/run.py scale "${@:2}"

  if [ "$1" != "no" ]; then
    checkout v3.4.1.post1 -mavx2
    ../../testsuite/run.py scale "${@:2}"
  fi

popd
