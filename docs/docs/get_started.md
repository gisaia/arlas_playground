# arlas_playground

## Clone the project

The **arlas_playground** project contains scripts and resources you need to run the tutorials.

Clone it in your working directory

```shell
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
- ARLAS Exploration Stack (Only to run ARLAS Locally)


## Python virtual environment

### Create the new environment

If it's the first time you run the project, create a virtual env before running the documentation.

Run at project root:

``` bash
python -m venv env_arlas_playground
```

Now the `env_arlas_playground` env exists and is stored at project root.

### Activate environment

To activate the environment in your terminal/powershell:

=== "Linux/Mac"
    
    ```commandline
    source env_arlas_playground/bin/activate
    ```

=== "Microsoft Windows Powershell"

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

Once the environment is activated, install the project dependency:

```
pip install -r requirements.txt
```

## Install and configure arlas_cli

`arlas_cli` is installed with the project requirements

```shell
pip install arlas_cli
```

Check if it is installed and that you have the latest version:

```shell
arlas_cli --version
```

By default, it is configured for a local ARLAS stack deployment.

To configure `arlas_cli` to access your ARLAS Cloud account, see [arlas_cli documentation](https://gisaia.github.io/arlas_cli/configuration/#arlas-cloud-configuration).

!!! warning 
    If `arlas_cli` is configured for ARLAS Cloud, the `--config` option in all tutorials `arlas_cli` commands must not be specified.

For more details, check the [full arlas_cli documentation](https://gisaia.github.io/arlas_cli/).

## Install and run ARLAS Exploration Stack

!!! warning
    You don't need to install and launch ARLAS Exploration Stack if you are using ARLAS Cloud.

To run the simplest ARLAS stack and Elasticsearch on the local machine, clone the [ARLAS Stack Exploration](https://github.com/gisaia/ARLAS-Exploration-stack) project and run the stack:

```shell
git clone https://github.com/gisaia/ARLAS-Exploration-stack.git
cd ARLAS-Exploration-stack
./start.sh
```

More details about the deployment can be found on the [ARLAS Stack Exploration project](https://github.com/gisaia/ARLAS-Exploration-stack).

## Now you can play

For the different examples, you will see how to:

- Get the spatio-temporal data
- Transform the data
- Index the data
- Set up a collection
- Set up a dashboard

You can now choose an example of ARLAS usage on spatio-temporal data:

- [AIS Vessels location](tutorials/ais/ais_tutorial.md)
