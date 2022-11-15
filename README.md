# My ChRIS Plugin

[![Version](https://img.shields.io/docker/v/fnndsc/ChRIS_Plugin?sort=semver)](https://hub.docker.com/r/fnndsc/ChRIS_Plugin)
[![MIT License](https://img.shields.io/github/license/fnndsc/ChRIS_Plugin)](https://github.com/FNNDSC/ChRIS_Plugin/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/ChRIS_Plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/ChRIS_Plugin/actions/workflows/ci.yml)

`ChRIS_Plugin` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Abstract

...

## Installation

`ChRIS_Plugin` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://ipfs.babymri.org/ipfs/QmaQM9dUAYFjLVn3PpNTrpbKVavvSTxNLE5BocRCW1UoXG/light.png)](https://chrisstore.co/plugin/ChRIS_Plugin)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `ChRIS_Plugin` as a container:

```shell
singularity exec docker://fnndsc/ChRIS_Plugin commandname [--args values...] input/ output/
```

To print its available options, run:

```shell
singularity exec docker://fnndsc/ChRIS_Plugin commandname --help
```

## Examples

`commandname` requires two positional arguments: a directory containing
input data, and a directory where to create output data.
First, create the input directory and move input data into it.

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
singularity exec docker://fnndsc/ChRIS_Plugin:latest commandname [--args] incoming/ outgoing/
```

## Development

Instructions for developers.

### Building

Build a local container image:

```shell
docker build -t localhost/fnndsc/ChRIS_Plugin .
```

### Running

Mount the source code `commandname.py` into a container to try out changes without rebuild.

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/commandname.py:/usr/local/lib/python3.10/site-packages/commandname.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/ChRIS_Plugin commandname /incoming /outgoing
```

### Testing

Run unit tests using `pytest`.
It's recommended to rebuild the image to ensure that sources are up-to-date.
Use the option `--build-arg extras_require=dev` to install extra dependencies for testing.

```shell
docker build -t localhost/fnndsc/ChRIS_Plugin:dev --build-arg extras_require=dev .
docker run --rm -it localhost/fnndsc/ChRIS_Plugin:dev pytest
```

## Release

Steps for release can be automated by [Github Actions](.github/workflows/ci.yml).
This section is about how to do those steps manually.

### Increase Version Number

Increase the version number in `setup.py` and commit this file.

### Push Container Image

Build and push an image tagged by the version. For example, for version `1.2.3`:

```
docker build -t docker.io/fnndsc/ChRIS_Plugin:1.2.3 .
docker push docker.io/fnndsc/ChRIS_Plugin:1.2.3
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/FNNDSC/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to a _ChRIS Store_.

```shell
docker run --rm localhost/fnndsc/ChRIS_Plugin:dev chris_plugin_info > chris_plugin_info.json
```

