.PHONY: clean setup lint env_test fuleCon_test lixtr_test lwd_test  

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROFILE = default
PROJECT_NAME = HYH
PYTHON_INTERPRETER = python

ifeq (,$(shell which conda))
	HAS_CONDA=False
else
	HAS_CONDA=True
endif

#################################################################################
# PROJECT GLOBAL SETUP                                                          #
#################################################################################


create_environment: ## Set up python interpreter environment
ifeq (True,$(HAS_CONDA))
		@echo ">>> Detected conda, creating conda environment."
	ifeq (3,$(findstring 3,$(PYTHON_INTERPRETER)))
		conda create --name $(PROJECT_NAME) python=3
	else
		conda create --name $(PROJECT_NAME) python=2.7
	endif
	@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)"
else
	$(PYTHON_INTERPRETER) -m pip install -q virtualenv virtualenvwrapper
	@echo ">>> Installing virtualenvwrapper if not already installed.\nMake sure the following lines are in shell startup file\n\
	export WORKON_HOME=$$HOME/.virtualenvs\nexport PROJECT_HOME=$$HOME/Devel\nsource /usr/local/bin/virtualenvwrapper.sh\n"
	@bash -c "source `which virtualenvwrapper.sh`;mkvirtualenv $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER)"
	@echo ">>> New virtualenv created. Activate with:\nworkon $(PROJECT_NAME)"
endif

setup: ## Setting up the project via setup.py
	$(PYTHON_INTERPRETER) -m pip install setuptools
	$(PYTHON_INTERPRETER) -m pip install -e .


clean: ## Delete all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


lint: ## Lint using flake8
	flake8 src/functions
	flake8 notebook

#################################################################################
# PROJECT TEST ROUTINGS                                                         #
#################################################################################

env_test: fuleCon_test lwd_test ## Test python, pulp and some internal packages.
	$(PYTHON_INTERPRETER) src/tests/env_tests.py

fuleCon_test: ## Test if <fuelCon> function working correctly.
	$(PYTHON_INTERPRETER) src/tests/fuel_consumption_tests.py


lwd_test: ## Test if <lwd> function is working correctly.
	$(PYTHON_INTERPRETER) src/tests/load_window_tests.py


lixtr_test: ## Test if <lixtr> function is working correctly. 
	$(PYTHON_INTERPRETER) src/tests/list_extraction_tests.py
