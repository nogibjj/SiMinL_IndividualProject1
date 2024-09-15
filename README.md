[![Lint](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/lint.yml)
[![Install](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/format.yml)
[![Test](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/SiMinL_IndividualProject1/actions/workflows/test.yml)

# Project 1: Continuous Integration using Gitlab Actions of Python Data Science Project

# Explanation Video
Please change the quality to the highest!
[[Link]](https://drive.google.com/file/d/1q251P57xbl9tSkWZlgIN6s9_FxiLMo-s/view?usp=drive_link)

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
├── test_lib.py
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

