# Python Project Local Setup in VS Code

This guide is for Python projects created inside:

```text
/Users/avinashanshu/vscode_workspace
```

The recommended setup is one virtual environment per project. This keeps each project's packages separate and prevents conflicts between projects.

## 1. Python installations

### Global Homebrew Python

The global Python installation on this Mac is:

```text
/opt/homebrew/bin/python3
```

Check it from any terminal:

```bash
which python3
/opt/homebrew/bin/python3 --version
```

This global Python is used to create project virtual environments. Project packages should normally be installed inside the project's `.venv`, not globally.

### Project-local Python

After creating a virtual environment for a project, its Python executable is normally:

```text
/Users/avinashanshu/vscode_workspace/<project_name>/.venv/bin/python
```

When the environment is activated, the commands `python` and `pip` point to this local environment.

Check the active interpreter:

```bash
which python
python --version
```

The result of `which python` should contain:

```text
/Users/avinashanshu/vscode_workspace/<project_name>/.venv/bin/python
```

## 2. Create a new project folder

Open a terminal and move to the workspace parent directory:

```bash
cd /Users/avinashanshu/vscode_workspace
```

Create and enter a new project folder. Replace `my_project` with the real project name:

```bash
mkdir my_project
cd /Users/avinashanshu/vscode_workspace/my_project
```

Confirm the current terminal location:

```bash
pwd
```

Expected result:

```text
/Users/avinashanshu/vscode_workspace/my_project
```

Open this folder in VS Code:

```bash
code /Users/avinashanshu/vscode_workspace/my_project
```

If the `code` command is not available, open the folder from VS Code using **File > Open Folder**.

## 3. Create the local virtual environment

Run this command while the terminal is located at the project folder:

```bash
/opt/homebrew/bin/python3 -m venv .venv
```

This creates:

```text
/Users/avinashanshu/vscode_workspace/my_project/.venv
```

Activate it in macOS zsh:

```bash
source /Users/avinashanshu/vscode_workspace/my_project/.venv/bin/activate
```

After activation, the terminal prompt usually starts with `(.venv)`.

Upgrade pip inside the local environment:

```bash
python -m pip install --upgrade pip
```

## 4. Install project packages

Always run package installation after activating `.venv` and while located at the project folder.

For a FastAPI project:

```bash
python -m pip install fastapi uvicorn
```

For a project with a dependency file:

```bash
python -m pip install -r requirements.txt
```

Save the installed packages for repeatable setup:

```bash
python -m pip freeze > requirements.txt
```

The resulting file is located at:

```text
/Users/avinashanshu/vscode_workspace/my_project/requirements.txt
```

## 5. Select the local interpreter in VS Code

In VS Code:

1. Open the Command Palette with `Cmd+Shift+P`.
2. Run `Python: Select Interpreter`.
3. Select:

```text
/Users/avinashanshu/vscode_workspace/my_project/.venv/bin/python
```

You can verify the selected interpreter in the VS Code status bar or by opening a new integrated terminal and running:

```bash
which python
```

If VS Code does not show the environment, choose **Enter interpreter path** and select:

```text
/Users/avinashanshu/vscode_workspace/my_project/.venv/bin/python
```

## 6. Run a FastAPI application

For a file named `first_api.py` containing an object named `app`, first move to the folder containing that file:

```bash
cd /Users/avinashanshu/vscode_workspace/my_project
source /Users/avinashanshu/vscode_workspace/my_project/.venv/bin/activate
```

Start Uvicorn:

```bash
uvicorn first_api:app --reload
```

The format is:

```text
uvicorn <python_module_name>:<application_object_name> --reload
```

For `first_api.py` and `app`, use:

```text
first_api:app
```

Do not include `.py` in the Uvicorn module name. For example, do not use `first_api.py:app`.

Open the application at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

Stop the server with `Ctrl+C`.

## 7. Current project example

For the current project, the folder is:

```text
/Users/avinashanshu/vscode_workspace/python_fast_api
```

Run these commands from any terminal to set it up:

```bash
cd /Users/avinashanshu/vscode_workspace/python_fast_api
/opt/homebrew/bin/python3 -m venv .venv
source /Users/avinashanshu/vscode_workspace/python_fast_api/.venv/bin/activate
python -m pip install fastapi uvicorn
uvicorn first_api:app --reload
```

The local interpreter is:

```text
/Users/avinashanshu/vscode_workspace/python_fast_api/.venv/bin/python
```

The application file is:

```text
/Users/avinashanshu/vscode_workspace/python_fast_api/first_api.py
```

## 8. Global installation versus local installation

There are three different locations that can be involved:

| Purpose | Location | Use |
|---|---|---|
| Global Python executable | `/opt/homebrew/bin/python3` | Create virtual environments and run general Python commands |
| Project-local Python | `/Users/avinashanshu/vscode_workspace/<project_name>/.venv/bin/python` | Run that project's code and packages |
| pipx application environment | `~/Library/Application Support/pipx/venvs/<application>/` | Isolated command-line applications such as Uvicorn |

`pipx` is not required for normal project development. It creates a separate environment for the installed application. Therefore, a Uvicorn installed with pipx may not see FastAPI installed in Homebrew Python or in a project's `.venv`.

For project work, use the local environment consistently:

```bash
source /Users/avinashanshu/vscode_workspace/<project_name>/.venv/bin/activate
python -m pip install fastapi uvicorn
python -m uvicorn first_api:app --reload
```

Using `python -m uvicorn` is especially clear because it guarantees that Uvicorn is run by the currently active Python environment.

## 9. Starting work on an existing project

Each time you reopen a project, run:

```bash
cd /Users/avinashanshu/vscode_workspace/<project_name>
source /Users/avinashanshu/vscode_workspace/<project_name>/.venv/bin/activate
which python
python -m pip install -r requirements.txt
python -m uvicorn first_api:app --reload
```

If the project does not yet have `requirements.txt`, install the required packages and create it:

```bash
python -m pip install fastapi uvicorn
python -m pip freeze > requirements.txt
```

When finished, leave the local environment with:

```bash
deactivate
```

## 10. Common problems

### `ModuleNotFoundError: No module named 'fastapi'`

The command is using a Python environment where FastAPI is not installed. Check the active interpreter:

```bash
which python
python -m pip show fastapi
```

If the project `.venv` is not active, activate it from the project folder:

```bash
source /Users/avinashanshu/vscode_workspace/<project_name>/.venv/bin/activate
```

Then install FastAPI into that environment:

```bash
python -m pip install fastapi
```

### `Attribute "app" not found in module`

Check all of the following:

- The file is named correctly, for example `first_api.py`.
- The application object is named `app`.
- The command is run from the directory containing the file.
- The command uses `first_api:app`, without `.py`.
- The file imports and creates FastAPI correctly:

```python
from fastapi import FastAPI

app = FastAPI()
```

### `uvicorn: command not found`

Activate the project environment and install Uvicorn:

```bash
cd /Users/avinashanshu/vscode_workspace/<project_name>
source /Users/avinashanshu/vscode_workspace/<project_name>/.venv/bin/activate
python -m pip install uvicorn
```

Then use the module form, which does not depend on a separate global command:

```bash
python -m uvicorn first_api:app --reload
```

## Quick rule

For every new Python project inside `vscode_workspace`:

```bash
cd /Users/avinashanshu/vscode_workspace/<project_name>
/opt/homebrew/bin/python3 -m venv .venv
source .venv/bin/activate
python -m pip install <packages>
python -m <module_or_server_command>
```
