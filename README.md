# Project Template

`project-temp` – this is my project template that enhances development experience in VS Code with streamlined features.

# How to use
1. Use this template to create a new repository and clone it

```bash
git clone https://github.com/AdamZh0u/<your-repo-name>.git
```

2. Install dependencies

```bash
uv sync
uc sync --group <docs/dev/...> # Optional: sync different groups of dependencies

# activate env in terminal
source .venv/bin/activate # mac linux
.venv/Scripts/activate # windows
```

3. (Optional) modify the pyproject.toml
* project name and license
* uv cache-dir settings
    - https://github.com/astral-sh/uv/issues/7285

```toml
[tool.uv]
cache-dir = ".uv" # need to make sure that the cache is on the same disk.
```

* install pre-commit hooks

```bash
uv tool run pre-commit
```

# Key Features

* VS Code workspace settings
    * Accessing the project root as a constant at `src/config.py`
    * Add working directory to python path so that the scripts can be run from source directory.
* uv for python package management
* configs loading
* pre-commit hooks
* mkdocs for documentation
* docker compose
* Jupyter Settings
    - Run Jupyter notebooks from the project root.
    - Enable the interactive mode for development.
* pytest + allure
* python modules
    - plot utils
    - database utils
* github actions
    - test
    - release
* commit message
    - [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
        - vscode extension: [Conventional Commits](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits)
    - commitizen
    - `cz bump --changelog` for updating changelog

## Settings

* Load Parameters from the `.env` file
    - In debug mode, parameters are loaded automatically.
    - Running in the terminal mode need user settings `"python.experiments.optInto": ["pythonTerminalEnvVarActivation"]`

## MkDocs

```bash
mkdocs new [dir-name] # create a new project

# start the live-reloading docs server
mkdocs serve -f docs/mkdocs.yml
```

## Github Actions

* test locally
    - act
* release-please
    - [release-please](https://github.com/googleapis/release-please)
    - put github token in repo secrets


# Reference
* [VS Code Python Environments Documentation](https://code.visualstudio.com/docs/python/environments#_creating-environments)
* [VS Code Python Issue #944](https://github.com/microsoft/vscode-python/issues/944)
