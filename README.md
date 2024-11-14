# arlas_playground

## Get the project:

```shell
cd -
git clone git@github.com:gisaia/arlas_playground.git
cd arlas_playground
```

## Prerequisite

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

It is also needed to create a virtual environment and to install the python requirements in `requirements.txt`.

## Create/Activate python environment

If it's the first time you run the project, create a virtual env before running the documentation.

Run at project root:

``` bash
python -m venv env_arlas_playground
```

Now the `env_arlas_playground` env exists and is stored at project root.

To activate the environment in your terminal:

### On Linux/Mac:
```commandline
source env_arlas_playground/bin/activate
```

### On Microsoft Window Powershell:
```commandline
env_arlas_playground\Scripts\Activate.ps1
```

On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. 

You can do this by issuing the following PowerShell command:
```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
See [venv documentation](https://docs.python.org/3.10/library/venv.html#creating-virtual-environments) for more information.

## Install python dependencies in the environment

Once the environment is activated:

```
pip install -r requirements.txt
```

## Install arlas_cli:

```shell
pip install arlas_cli
```

Check you have the latest version:

```shell
arlas_cli --version
```

Check [here](https://pypi.org/project/arlas-cli/#history) the available version and here the [full documentation](https://gisaia.github.io/arlas_cli/).

## Install and run ARLAS Exploration Stack:

To run the simplest ARLAS stack and elasticsearch on the local machine, clone the [ARLAS Stack Exploration](https://github.com/gisaia/ARLAS-Exploration-stack) project and run the stack:

```shell
git clone https://github.com/gisaia/ARLAS-Exploration-stack.git
cd ARLAS-Exploration-stack
./start.sh
```

More details about deployment can be found on [ARLAS Stack Exploration project](https://github.com/gisaia/ARLAS-Exploration-stack).

## Now you can play ...

For the different examples, you will see how to:
- Get the spatio-temporal data
- Transform the data
- Index the data
- Set up a collection
- Set up a dashboard

You can now choose an example of ARLAS usage on spatio-temporal data:
- [Météo France Climatological data](meteo_france/README.md)
- [AIS Vessels location](ais/README.md)
- [Sun potential of buildings roofs](sunny_osm/README.md)
