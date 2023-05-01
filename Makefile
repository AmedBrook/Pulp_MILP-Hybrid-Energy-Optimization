.PHONY: clean setup lint env_test fuleCon_test lixtr_test lwd_test obj_test 

#################################################################################
# GLOBALS.                                                                      #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROFILE = default
PROJECT_NAME = HEO
PYTHON_INTERPRETER = python

ifeq (,$(shell which conda))
	HAS_CONDA=False
else
	HAS_CONDA=True
endif

#################################################################################
# PROJECT GLOBAL SETUP.                                                         #
#################################################################################

setup: ## Setting up the project via setup.py
	$(PYTHON_INTERPRETER) -m pip install setuptools
	$(PYTHON_INTERPRETER) -m pip install -e .


clean: ## Delete all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


lint: ## Lint using flake8
	$(PYTHON_INTERPRETER) -m flake8 src/functions
	$(PYTHON_INTERPRETER) -m flake8 notebooks
	$(PYTHON_INTERPRETER) -m flake8 models
	$(PYTHON_INTERPRETER) -m flake8 tests

#################################################################################
# PROJECT TEST UNITS.                                                           #
#################################################################################

env_test: fuleCon_test lwd_test ## Test python, pulp and some internal packages.
	$(PYTHON_INTERPRETER) tests/env_tests.py

fuleCon_test: ## Test if <fuelCon> function working correctly.
	$(PYTHON_INTERPRETER) tests/fuel_consumption_tests.py

lwd_test: ## Test if <lwd> function is working correctly.
	$(PYTHON_INTERPRETER) tests/load_window_tests.py

lixtr_test: ## Test if <lixtr> function is working correctly. 
	$(PYTHON_INTERPRETER) tests/list_extraction_tests.py

obj_test: ## Test if the <Objective function> returns accuarate fuel values.
	$(PYTHON_INTERPRETER) tests/obj_test.py
