# Project 1: Continuous Integration using Gitlab Actions of Python Data Science Project

# Youtube Video

# Directory
SiMinL_IndividualProject1/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── mylib/
│   ├── __init__.py
│   └── lib.py
├── .gitignore
├── returnvsrisk.png
├── rollingaverage.png
├── stocks.md
├── stocks.csv
├── Dockerfile
├── main.py
├── Makefile
├── README.md
├── repeat.sh
├── requirements.txt
├── setup.sh
├──test_lib.py
└── test_main.py

# Requirements
The project structure must include the following files:
- Jupyter Notebook with: 
1. Cells that perform descriptive statistics using Polars or Panda.
2. Tested by using nbval plugin for pytest
- Makefile with the following:
1. Run all tests (must test notebook and script and lib)
2. Formats code with Python black
3. Lints code with Ruff
4. Installs code via:  pip install -r requirements.txt

test_script.py to test script
test_lib.py to test library
Pinned requirements.txt
Gitlab Actions performs all four Makefile commands with badges for each one in the README.md

