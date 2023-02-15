.PHONY: help clean setup lint test_env test_fuleCon test_lixtr test_lwd 

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

test_env: test_fuleCon test_lwd ## Test python, pulp and some internal packages.
	$(PYTHON_INTERPRETER) test_environment.py

test_fuleCon: ## Test if <fuelCon> function working correctly.
	$(PYTHON_INTERPRETER) src/tests/fuel_consumption_tests.py


test_lwd: ## Test if <lwd> function is working correctly.
	$(PYTHON_INTERPRETER) src/tests/load_window_tests.py


test_lixtr: ## Test if <lixtr> function is working correctly. 
	$(PYTHON_INTERPRETER) src/tests/list_extraction_tests.py


#################################################################################
# SELF DOCUMENTTING COMMANDS                                                   #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>


help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
