# Project Template

`project-temp` – this is my project template that enhances development experience in VSCode with streamlined features.

# How to use
1. Clone the repository

```bash
git clone https://github.com/your-username/project-temp.git
```

2. Install dependencies

```bash
uv sync

# activate env
source ./.venv/bin/activate
```

# Features

## settings

* Accessing the project root as a constant.
* Load Parameters from the `.env` file
    - In debug mode, parameters are loaded automatically.
    - Running in the terminal mode need user settings `"python.experiments.optInto": ["pythonTerminalEnvVarActivation"]`

## python modules

* Plot utils
* Databse utils

## Tools

### docker for development

* Docker
    - Build docker image

```bash
docker compose up -d
```

### uv - python package manager

* uv

```bash
source .venv/bin/activate
```

### tests

* pytest + allure

### docs

* mkdocs

```bash
mkdocs new [dir-name] # create a new project

# start the live-reloading docs server
mkdocs serve -f docs/mkdocs.yml
```

* mathjax support
* mkdocstrings-python

    - demo
    - [Google Style Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

* gen-files

    - [gen-files](https://mkdocstrings.github.io/recipes/)

### jupyter

* Jupyter Settings
    - Run Jupyter notebooks from the project root.
    - Enable the interactive mode for development.

## pre-commit

* pre-commit

```bash
pre-commit install

# run pre-commit
pre-commit run --all-files
```

## github actions

* test locally
    - act
* release-please
    - [release-please](https://github.com/googleapis/release-please)
    - put github token in repo secrets
* commit message
    - [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
        - vscode extension: [Conventional Commits](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits)
    - commitizen
    - `cz bump --changelog` for updating changelog

# Reference
* [VS Code Python Environments Documentation](https://code.visualstudio.com/docs/python/environments#_creating-environments)
* [VS Code Python Issue #944](https://github.com/microsoft/vscode-python/issues/944)
