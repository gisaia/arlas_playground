# arlas_playground

## Clone the project

The **arlas_playground** ([repo](https://github.com/gisaia/arlas_playground){:target="_blank"}) project contains scripts and resources you need to run the tutorials.

Clone it in your working directory:

```shell
git clone git@github.com:gisaia/arlas_playground.git
cd arlas_playground
```

!!! tip
    To add the project root to your PYTHONPATH, simply run in your terminal:
    ```shell
    export PYTHONPATH="$(pwd):$PYTHONPATH"
    ```

    It can be added permanently to your shell configuration file (.bashrc, .bash_profile, or .zshrc) 
    

## Prerequisite

This repo illustrates a couple of usages of ARLAS. In order to play with it, you'll need:

- git version (>=2.39.3)
- python 3.10
- curl (>=8.4.0)

## Python virtual environment

If it's the first time you run the project, create a virtual env before running the documentation.

Run at project root:

``` bash
python -m venv env_arlas_playground
```

!!! success
    Now the `env_arlas_playground` env exists and is stored at project root.

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

See [venv documentation](https://docs.python.org/3.10/library/venv.html#creating-virtual-environments){:target="_blank"} for more information.

Once the environment is activated, install the project dependency:

```
pip install -r requirements.txt
```

## ARLAS Instance

The tutorials require ARLAS up and running.

ARLAS can be managed or deployed locally:

- **ARLAS Cloud**: The simplest way to access ARLAS is to create an ARLAS Cloud account. See [ARLAS Cloud Guide](../../static_docs/arlas_cloud.md)
- **Local ARLAS**: To run a simple ARLAS stack and Elasticsearch on the local machine, follow the [Deploying ARLAS Guide](../../external_docs/ARLAS-Exploration-stack/arlas_exploration_stack.md).


## Install and configure arlas_cli

Install `arlas_cli` with pip:

```shell
pip install arlas_cli
```

To ensure that it is installed and that you have the latest version, run:

```shell
arlas_cli --version
```

=== "ARLAS Cloud"
    To configure `arlas_cli` to access your ARLAS Cloud account, see [ARLAS CLI cloud configuration guide](../../external_docs/arlas_cli/configuration.md/#arlas-cloud-configuration).


=== "Local ARLAS"

    When installed, `arlas_cli` is configured for a local ARLAS stack deployment.

    To make sure that the `local` configuration is set as default, run:

    ```
    arlas_cli confs set local
    ```

For more details, check the [full arlas_cli documentation](../../external_docs/arlas_cli/index.md).


## Now you can play

For the different examples, you will see how to:

- Get the spatio-temporal data
- Transform the data
- Index the data
- Set up a collection
- Set up a dashboard

You can now choose an example of ARLAS usage on spatio-temporal data:

- [AIS Vessels location](tutorials/ais/ais_tutorial.md)
- [Sun potential of buildings roofs](tutorials/sunny_osm/sunny_osm_tutorial.md)
- [Earth Observation detected objects](tutorials/eo_objects/eo_objects_tutorial.md)
