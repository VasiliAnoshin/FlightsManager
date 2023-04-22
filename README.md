# FlightsManager 💡
 
## run project in virtual environment 🚀

- Create virtual env:

```bash
        python -m virtualenv <folder_name>
```

- Create virtual environment version depend:

```bash
        virtualenv <folder_name> --python=python3.9
```

- activate

```bash
  .\<folder_name>\Scripts\activate.bat
```

- ctrl + shift + p: Python: Select interpreter
  should include Python interpreter related to your environment
- refresh terminal
- install requirements:
  There exist two requirements files one for production and one for development.

```bash
        pip install -r <Path_to_file>\requirements-dev.txt
```

- deactivate:

```bash
        deactivate
```