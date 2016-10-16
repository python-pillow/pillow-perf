#!/bin/bash -ex

cd "$(dirname "$0")"

sudo apt-get install python-virtualenv

mkdir -p ~/env/pillow-perf
rm -rf ~/env/pillow-perf
virtualenv ~/env/pillow-perf
source ~/env/pillow-perf/bin/activate

pip install --upgrade pip

git clone https://github.com/uploadcare/pillow-simd.git Pillow || true

pushd Pillow

  git fetch

  function checkout {
    git checkout -f $1
    touch ./_imaging.c
    CFLAGS="$2" python ./setup.py develop
  }

  checkout 2.6.2
  ../../testsuite/run.py scale "$@"
  
  checkout 2.7.0
  ../../testsuite/run.py scale "$@"

  checkout 3.3.3
  ../../testsuite/run.py scale "$@"

  checkout 3.4.1
  ../../testsuite/run.py scale "$@"

  checkout v3.2.0.post3 -msse4
  ../../testsuite/run.py scale "$@"

  checkout v3.2.0.post3 -mavx2
  ../../testsuite/run.py scale "$@"

  checkout v3.3.3.post0 -msse4
  ../../testsuite/run.py scale "$@"

  checkout v3.3.3.post0 -mavx2
  ../../testsuite/run.py scale "$@"

  checkout v3.4.1.post1 -msse4
  ../../testsuite/run.py scale "$@"

  checkout v3.4.1.post1 -mavx2
  ../../testsuite/run.py scale "$@"

popd
