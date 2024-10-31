# arlas_playground

This repo illustrates a couple of usages of ARLAS. In order to play with it, you'll need:

- git version (>=2.39.3)
- docker (>=27.0.3)
- docker compose
- python 3.10
- curl (>=8.4.0)
- csvkit (>=1.4.0)
- jq (>=1.7.1)

Run `./check_requirements.sh` to check these requirements.

Then, we'll also install:
- arlas_cli
- ARLAS Exploration Stack

## Insall arlas_cli:

```shell
pip install arlas_cli
```

Check you have the latest version:

```shell
arlas_cli --version
```

Check [here](https://pypi.org/project/arlas-cli/#history) the available version and here the [full documentation](https://gisaia.github.io/arlas_cli/).

## Insall and run ARLAS Exploration Stack:

```shell
git clone git@github.com:gisaia/ARLAS-Exploration-stack.git
cd ARLAS-Exploration-stack
./start.sh
```

## Get the project:

```shell
cd -
git clone git@github.com:gisaia/arlas_playground.git
cd arlas_playground
```

## Now you can play ...

For the different examples, you will see how to:
- get the spatio-temporal data
- transform the data
- index the data
- setup a collection
- setup a dashboard

You can now choose an example of ARLAS usage on spatio-temporal data:
- [Méto France Climatological data](meteo_france/README.md)
