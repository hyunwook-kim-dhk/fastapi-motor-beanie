# FastAPI Motor Skeleton

## Project Setup

Check the python version first. The version should be same as [.python-version](./.python-version).

```shell
python --version
```

Then you can install dependencies by using [Poetry](https://python-poetry.org/).

```shell
poetry install
```

This command will create ".venv" in your current working directory.

To use virtualenv, you can run

```shell
source .venv/bin/activate
```

Or you can setup your IDEs with the ".venv" directory.

After you succeed to install every dependency, you are ready to develop!

## Testing Suites

This project includes the following steps to test.

- flake8 : source code format
- black : source code format
- isort : import order
- pylint : static analysis
- mypy : type check
- pytest : automatic test
- coverage : automatic test coverage

You can find the more detail in [./test.sh](./test.sh) file.

## Test with Minikube and Skaffold

This project uses [Minikube](https://minikube.sigs.k8s.io/) and [Skaffold](https://skaffold.dev/) to improve the local development environments.

You can deploy and test the service in your Minikube cluster.

```shell
skaffold delete
skaffold run --tail
minikube tunnel -c
```

## Project Structures

The project includes the following files and modules.

### [app/start.py](./app/start.py)

This file includes the fast api application instance and defines the behavior when the fast api starts to run.

### [app/apis](./app/apis)

This module includes the every apis to provide in this service.

### [app/common](./app/common)

This module includes the common independent utils.

### [app/config](./app/config)

This module includes the [Setting](./app/config/setting.py) class. Setting class automatically loads the environment
variables.

### [app/modules](./app/modules)

This module includes the several sub-modules. The sub-modules aim to implement the domain specific logic.

### [app/setup](./app/setup)

This module includes the below setup files

- [database.py](./app/setup/database.py) : Setup database with [Setting](./app/config/setting.py) instance
- [middleware.py](./app/setup/middleware.py) : Setup fast api middleware such as CORS
- [service.py](./app/setup/service.py) : Initialize the services and inject the dependencies of them
