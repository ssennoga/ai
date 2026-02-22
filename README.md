# 1. Create project folder
mkdir ai && cd ai

# 2. Create virtual environment (best: uv or pdm or poetry)
# Option A - uv (fastest & most modern in 2025)
uv venv
source .venv/bin/activate

# Option B - built-in venv
python -m venv .venv
source .venv/bin/activate

output:
```shell
ai % uv venv 
Using CPython 3.13.2 interpreter at: /usr/local/opt/python@3.13/bin/python3.13
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

# 3. Install dependencies
uv pip install -r requirements.txt
# or with poetry:  poetry install

output:
```shell
uv pip install -r requirements.txt
Resolved 93 packages in 1.31s
Prepared 93 packages in 3.73s
Installed 93 packages in 475ms
 + aiohappyeyeballs==2.6.1
 + aiohttp==3.13.3
 + dataclasses-json==0.6.7
 + datasets==4.5.0
 + httpx==0.28.1
 .
 .
 ```

# If uv is not install it with brew:
```shell
brew install uv  
```

# Activate venv
```shell
source .venv/bin/activate
```


# Run
```shell
python src/main.py
```

## Troubleshooting
- If you encounter issues with the virtual environment, try deleting the `.venv` folder and creating it again with `uv venv`.
- Make sure you have Python 3.13 or higher installed on your system, as some dependencies may require it.
- If you are using a different package manager (like poetry or pipenv), adjust the commands accordingly to create the virtual environment and install dependencies.
- Always check the `requirements.txt` file for any specific versions of packages that may be required for compatibility.
- If you encounter any issues with package installations, try updating pip with `pip install --upgrade pip` and then reinstalling the dependencies.
- If your module is not found, ensure that your `PYTHONPATH` is set correctly to include the `src` directory where your modules are located. You can set it temporarily in the terminal with:
```shellexport PYTHONPATH=$(pwd)/src:$PYTHONPATH
```
Other options include adding an `__init__.py` file to your `src` directory to make it a package, or using relative imports in your code.
The ModuleNotFoundError: No module named 'src' error occurs because the Python interpreter does not know where to locate the 'src' directory. Python searches for modules in its system path (sys.path), and your project's src directory is not currently included.

Here are a few ways to resolve this issue:
1. Run your script as a module using `-m`
   Instead of running your script directly with python your_script.py, use the -m switch and run it as a module from the parent directory of src. This tells Python to add the current working directory to the system path, allowing it to find the src package.

   Correct Command (if your_script.py is inside the src folder): 
 ```shell 
python -m src.your_script
``` 

2. Add the parent directory of src to `PYTHONPATH`
   You can explicitly tell Python where to look for the 'src' module by adding its parent directory to the `PYTHONPATH` environment variable.
   Linux/macOS (current session)
```shell
export PYTHONPATH=$(pwd):$PYTHONPATH
```
   Windows (current session)
```shell
set PYTHONPATH=%cd%;%PYTHONPATH%
```
   After setting this, you can run your script normally:
```shell
python src/your_script.py
```

