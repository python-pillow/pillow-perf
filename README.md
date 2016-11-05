# Testsuites

[![Build Status](https://travis-ci.org/python-pillow/pillow-perf.svg?branch=master)](https://travis-ci.org/python-pillow/pillow-perf)

Performance tests divided into suites.

### Prerequisites

* [Any Pillow version](https://pillow.readthedocs.io/en/latest/installation.html#basic-installation)
* [ImageMagick dev package for Wand](http://docs.wand-py.org/en/0.4.3/#requirements)

### Install and run

```bash
$ cd testsuite
$ pip install -r ./requirements.txt
$ ./run.py [testsuite]
```

`[testsuite]` is one of available testsuites:

* convert
* scale
* blur
* composition
* wand_scale

The list can grow, please refer to:

```bash
$ ./run.py --help
```

### CLI

```bash
$ ./run.py scale --progress
$ ./run.py scale --mode RGBA
$ ./run.py scale --runs 50
$ ./run.py scale --size 512x512
```

For some suites the chosen mode (`scale`, `blur`) does matter,
while others (`convert`, `composition`) work regardless of current mode.


# Automatic test

Automatic test launches testsuites against relevant Pillow versions
including SSE4 and AVX2.
Currently it works only on Linux.

### Prerequisites

* git
* virtualenv
* grep
* ccache (optional)

### Run

```bash
$ cd auto
$ ./run.sh                # Run all tests
$ ./run.sh no             # Skip AVX2 tests
$ ./run.sh - -s 512x512   # Pass extra arguments to testsuite
$ ./run.sh no -s 512x512  # Pass extra arguments and skip AVX2 tests
$ CC="ccache cc" ./run.sh # Speed up subsequent builds using CC cache
```


# Docs

The docs can be found on the [public page](https://python-pillow.org/pillow-perf/)
with benchmark results and details.

### Build once

```bash
$ cd docs
$ npm install -g webpack
$ npm install
$ webpack --display-modules
```

### Serve local & rebuild

```bash
$ python -m SimpleHTTPServer &
$ webpack --display-modules -w
```
