# Getting started.  

For full source project : [https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization](https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization).



## Project layout.
---
    mkdocs/
        docs/
            img/
            javascripts/
                        mathjax.js
            ...
        site/
            ...
        mkdocs.yml
    models/
        .gitkeep
    notebooks/
            .gitkeep
            heo_model.ipynb
    references/
        .gitkeep
    reports/
        figures/
        Load Analysis & Benchmark/
        ...
    src/
        dataset/
        functions/
                 ...
            tests/
                env_tests.py
                fuel_consumption_tests.py
                list_Extraction_tests.py
                load_window_tests.py
        __init__.py
        .gitkeep
        add_dict.py
        fuel_consumption.py
        list_extraction.py
        load_window.py
        rand_val.py
        rand_window.py
    Authors.txt
    Changelog.md
    License
    Makefile
    Readme.md
    Requirements.txt
    setup.py
    setup.cfg

<br>
---
## Setup options.
---

### Standalone setup.
----

###### Environment.

* `$ conda create --HEO_model python=3.9.7` - Create a new environment aside of the root, and name it somthing recognisable, we named here as HEO_model, we have used here python version 3.9.7. to do so you tape.

###### Requirements and Dependencies.

 Before stating the setup process you need to have <em>`setuptools`</em> installed, if you don't have it already do through the following commands:

* Python package index (Pypi) : `$ pip install setuptools`

* Anaconda package index (Conda) : `$ conda install -c conda-forge setuptools`

 Now that you have <em>`setuptools`</em> in you environment, in order to install all packages and dependencies at once run the command : 

*  `$ python -m pip install -e .`

---
### Pre-configured setup.
----


While the manual installation can walk you through around the various commands basics for each used packages in the project, chances are you might already know those commands and you don't want to bother yourself about taping every single command, so that's why we have provided the possibility to use `make` scripting, to make life easy for you. You find in the following the commands you will need to do this. 


In case you have make installed in your system, for Linux based system it comes already installed in your system you don't need to install anything just skeep this part to {...}. For windows based systems there are multiple ways to get GNU make installed, like for example Cygwin, Nmake, Cmake..., however we recommand to go for [chocolatey](https://community.chocolatey.org/packages/make), we think it's the most straighforward way to install make for windows systems with less effort. 

#### chocolatey.


 First thing first, we will install chocolatey, make sure you are using the Powershell command as an admin,
	
* Then run this command first : 
```bash
Get-ExecutionPolicy 
```

* If it returns Restricted, then run : 
```bash
Set-ExecutionPolicy AllSigned or Set-ExecutionPolicy Bypass -Scope Process
```

* Now, to install `chocolatey` run the following command by coping it at once and past it in command line, then hit enter:

```bash
 Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) 

```

Please check [chocolatey](https://community.chocolatey.org/packages/make) website for more guidance !
    

#### Make.


* Now that you have `chocolatey` installed, we can install `make` by running the command : 

``` 
     $ choco install make --version=3.81
```

Once make installation is done, and assuming that you have downloaded the project files in your local machine it's very easy to workout everything. 

* To create the conda environment run the command : 
 
```	
	 $ make create_environment
```

* To setup the project run the command : 

``` 
	 $ make setup
```

##### Mathjax. 

Mathjax is a Javascript library that can display mathimatical notations in the browser using LaTex or other. 
In order to integarate Mathjax within Mkdocs do the following: 

* Install pymdown-extensions (Pypi): `$ python -m pip install pymdown-extensions` 

* Within your mkdocs folder create the following: 

```
 			mkdocs_______
      			|___ docs
		      			|___ javascripts
             			|     		|___ mathjax.js
			    		|           
```									


* Add the following script lines in the configuration file `mkdocs.yml` :

```yaml
extra_javascript:

    javascripts/mathjax.js
    https://polyfill.io/v3/polyfill.min.js?features=es6
    https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

----
## Testing units.
----

#### Testing the environment.


* To test packages and dependencies just run the command : 

```	
	- $ make env_test
```
Behind the scenes, make will go over the `Makefile` located in our directory which itself will chain to all test units located in `/src/tests` directory and execute every single test module existing in that directory.

----

#### Testing syntax & style.

* To lint code scripts we are using flake8, just run the following command : 

```	
	 - $ make lint
```
Under the hood, make will go over the `Makefile` located in our directory which itself will chain to all coding resources in `/src/functions` and `/notebooks` directories and will check the syntax and style of your code using flake8 to meet PEP8 standards.


#### Testing internal modules. 

In our code we ended up using three main functions which help us to implemente the problem, the first function is called `FuelCon` it is used to calculate based on a linear model the fuel comsumption of the genset for a specific power load `P`. The second function is called ``lwd`, is the abreviation of load window, which is used to constructe a load profile for a specific number of time steps out of a given sets of power loads arrays. The third one is called `lixtr` and it's the abreviation of list extraction, which could be used in the section 'Pre-processing visualization data' for extracting lists out of dictionaries. So in order to make sure those functions are behaving as is should be some testing routings are required by following the next commands. 

* To test the `FuelCon` function, run the command: 

```	
	 - $ make fuelCon_test
```

* To test the `lwd` function, run the command: 

```	
	 - $ make lwd_test
```

* To test the `lixtr` functions, run the command: 

```	
    - $ make lixtr_test
```

