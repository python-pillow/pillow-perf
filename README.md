# Run testsuite

Prerequirements:

* [Any Pillow version](https://pillow.readthedocs.io/en/3.4.x/installation.html#basic-installation).
* [ImageMagick dev package for wand](http://docs.wand-py.org/en/0.4.3/#requirements)

Install and run:

```bash
$ cd testsuite
$ pip install -r ./requirements.txt
$ ./run.py [testsuite]
```

Testsuite CLI:

```bash
$ ./run.py scale --progress
$ ./run.py scale --mode RGBA
$ ./run.py scale --runs 50
$ ./run.py scale --size 512x512
```


# Build docs

Build the project once:

```bash
$ cd docs
$ npm install -g webpack
$ npm install
$ webpack --display-modules
```

Serve local with on the fly rebuild.

```bash
$ python -m SimpleHTTPServer &
$ webpack --display-modules -w
```
