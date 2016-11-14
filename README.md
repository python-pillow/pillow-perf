# Test Suites

[![Build Status](https://travis-ci.org/python-pillow/pillow-perf.svg?branch=master)](https://travis-ci.org/python-pillow/pillow-perf)

Performance tests divided into suites.

### Prerequisites

* [Any Pillow version](https://pillow.readthedocs.io/en/latest/installation.html#basic-installation)
* [ImageMagick dev package for Wand](http://docs.wand-py.org/en/0.4.3/#requirements)

### Install and run

```bash
$ cd testsuite
$ pip install -r ./requirements.txt
$ ./run.py test_suite [test_suite ...]
```

`test_suite` is one of available test suites:

* load
* convert
* rotate_right
* scale
* blur
* composition
* wand_load
* wand_rotate_right
* wand_scale
* cv2_load
* cv2_rotate_right
* cv2_blur

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

Automatic test launches test suites against relevant Pillow versions
including SSE4 and AVX2.
Currently it works only on Linux Ubuntu.

You have two ways to run the test:
Vagrant or host (tested on Ubuntu 14.04 and 16.04).

### Run in Vagrant

Please, ensure that you are using Vagrant version 1.8.7 or latter.

```bash
$ cd auto
$ vagrant up
```

It will automatically start a full test
which can took over 10 minutes.
Run the test again:

```bash
$ vagrant provision --provision-with run
```

### Run on the host

First you need to install the prerequisites:

```bash
$ cd auto
$ sudo ./install_ubuntu.sh
```

Script options:

```bash
$ cd auto
$ ./run.sh                # Run all tests
$ ./run.sh no             # Skip AVX2 tests
$ ./run.sh - --json       # Pass extra arguments to test suite
$ ./run.sh no --json      # Pass extra arguments and skip AVX2 tests
$ CC="ccache cc" ./run.sh # Speed up subsequent builds using CC cache
```

### Submit results

We are highly concerned in tests on latest AMD CPU.

1. Before run any tests, please ensure that
you have exited all browsers on host machine,
closed all audio players and stopped backup system.

2. Run [automatic test](#automatic-test) using
default `--size`, `--mode` and `--runs` settings.
Also, please include `--json` option.

3. Collect the following information about your system:
name, OS version, CPU. For example:

    * Name: MacBook Pro (Retina, 13-inch, Late 2013)
    * OS: Ubuntu 14.04.4 LTS 64bit
    * CPU: Intel® Core™ i5-4258U CPU @ 2.40GHz

4. Create an [issue](https://github.com/python-pillow/pillow-perf/issues)
with collected information and test output.


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
