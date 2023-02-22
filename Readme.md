HYH
==============================

PuLP-MILP Hybrid Energy Optimization.

$\newline$  
$\newline$ 
Project's title.
=================


Fuel minimization: MILP model with semi-continuous power supply and battery logic.

Project's description and context. 
===============================


The project aims to explore the possibility of integrating 
energy storage faciltities within the shipping industry marcket. 
In this application we simulate one possible solution on how to
synchronize fuel based gensets with a battery storage system
alonge side with energy optimization to reduce energy cost throughout the trip journey. The whole project is build based on an optimization mathimatical model and uses MILP (mixed intiger linrear programing) methodes to solve optimaly the problem.  

In the Notebook scripts associated with this porject, we simulate an application used to optimize fuel consumption for vessels using one genset to produce the required energy and one battery storage system to store and realese the excess of that energy when needed in a hybrid mode.

The framwork used in this case study is PuLP, to solve a Mixed Intger Linear Programming problem together with first the built-in solver CBC and then with a commercial solver, we used Gurobi in our case.

Project use case.
====================

this particular case is initially specefic for the offshore shipping industry as they are the most transportation fuel consuming and needing some sort of solutions to use fuel  optimally in their trips. However this is not only exlusive to this sector, it can be easily extended to other sectors as long as the purpose is to optimize energy usage and energy hybridization.

$\newline$  
$\newline$ 
  ##  <em> Installations walk-through. </em>  

> This is a quick guide on how to install the required packages if you have decided for whatever reason to go through installations one by one and setting up the project without passingg by the setup.py file. Though you still have to go through the manual installation for [Mathjax](https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization#mathjax) setup. 
>$\newline$  
>$\newline$  
### matplotlib.
------------
>
>- In order to install matplotlib package run one of the following commands : : 
>
>Using Anaconda package index :
>```
>	- $ conda install -c conda-forge matplotlib
>```
>Using Python package index (Pypi) : 
>```
>	- $ python -m pip install matplotlib
>```

### numpy.
------------
>
>- In order to install numpy package run one of the following commands : : 
>
>Using Anaconda package index :
>```
>	- $ conda install -c anaconda numpy
>```
>Using Python package index (Pypi) : 
>```
>	- $ python -m pip install numpy

### PuLP.
------------
>
>- In order to install Pulp modler packages run one of the following commands : : 
>
>Using Anaconda package index :
>```
>	- $ conda install -c forge-pulp
>```
>Using Python package index (Pypi) : 
>```
>	- $ python -m pip install pulp
>```

### Gurobi. 
-------------
>
- To install Gurobi solver packages, run one of the following commands :
>
> Using Anaconda package index :
>```	
>	- $ conda install -c gurobi gurobi  
>```
> Using Python package index (Pypi) : 
>```
>	- $ python -m pip install gurobipy 
>```

### Mkdocs. 
------
- To install Mkdocs packages, run one of the following commands :
>  
Using Python package index (Pypi) : 
>```	
>	- $ python -m pip install mkdocs
>```
Using Anaconda package index :
>```	
>	- $ conda install -c conda-forge mkdocs
>```
>
 - To create new mkdocs project : 
> ```	
>	- $ python -m mkdocs new [name of the project]
> ```
> - To preview your documentation, you need to locate in the docs directory created with the last command and then run: 
> ```	
>	- $ python -m mkdocs serve 
> ```	
 - To preview the documentation then browse within the output https address returned by the last command.
>
> For more guidance on mkdocs, see [here](https://www.mkdocs.org/user-guide/).
>

### Mathjax. 
-------
Mathjax is a Javascript library that can display mathimatical notations in the browser using LaTex or other. 
In order to integarate Mathjax within Mkdocs do the following: 
>
> - Install pymdown-extensions (Pypi): 
>
> ```	
>	- $ python -m pip install pymdown-extensions
> ```
> - Within your mkdocs folder create the following: 
>
> ```
>  			mkdocs_______
>      			|___ docs
>		      			|___ javascripts
>             			|     		|___ mathjax.js
>			    		|           
>									
>```
>
> - Add the following script lines in the configuration file<em><strong> `mkdocs.yml` </em></strong>
>
> ```
>extra_javascript:
>
>javascripts/mathjax.js
>https://polyfill.io/v3/polyfill.min.js?features=es6
>https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
>
>```

### flake8. 
-----
> To analyse code syntax and debug make sure each single peace of code follows the PEP8 and other coding standards we use flake8 linter to do so. 
>- In order to install flake8 run on of the follwing commands : 
>
>Using Anaconda package index :
>```
>	- $ conda install -c anaconda flake8
>```
>Using Python package index (Pypi) : 
>```
>	- $ python -m pip install flake8
>```
>
$\newline$  
$\newline$ 

---
## Project setup options. 
---
###  Standalone setup.
>$\newline$  
>$\newline$ 
>
#### Environment.
---
>
- Using Anaconda environnment manager: 
>
 You create a new environment, and called somthing recognisable, we named it here as <em>HYH</em> , we have used here python version 3.9.7. to do so you tape : 
> ```
>	- $ conda create --HYH python=3.9.7
>```
> - Activate the environment by taping :
> ```
>	- $ conda activate --HYH_env.
> ```
>$\newline$  
>$\newline$ 
#### Requirements & Dependencies.
---
>
> Before stating the setup process you need to have <em>`setuptools`</em> installed, if you don't have it already do so,
> run the command :
> - Through Pypi : 
>```
>	- $ pip install setuptools 
>```
> - Through Conda :
>```
>	- $ conda install -c conda-forge setuptools 
>```
> - Now that you have <em>`setuptools`</em> in you environment, in order to install all packages and dependencies at once run the command : 
>
>```
>	- $ python -m pip install -e . 
>```
> 
$\newline$  
$\newline$ 
### Pre-configured setup.
----


While the manual installation can walk you through around the various commands basics for each used packages in the project, chances are you might already know those commands and you don't want to bother yourself about taping every single command, so that's why we have provided the possibility to use <em><strong>`make`</em></strong> scripting, to make life easy for you. You find in the following the commands you will need to do this. 


In case you have make installed in your system, for Linux based system it comes already installed in your system you don't need to install anything just skeep this part to {...}. For windows based systems there are multiple ways to get GNU make installed, like for example Cygwin, Nmake, Cmake..., however we recommand to go for [chocolatey](https://community.chocolatey.org/packages/make), we think it's the most straighforward way to install make for windows systems with less effort. 

$\newline$  
$\newline$ 
#### chocolatey.
--------------
>
> First thing first, we will install chocolatey, make sure you are using the Powershell command as an admin,
>	
- Then run this command first :
>```
> Get-ExecutionPolicy 
>```
- If it returns Restricted, then run : 
>```
> Set-ExecutionPolicy AllSigned or Set-ExecutionPolicy Bypass -Scope Process
>```
- Now, to install `chocolatey` run the following command by coping it at once and past it in command line, then hit enter:
>
>```
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
>```
>
Please check [chocolatey](https://community.chocolatey.org/packages/make) website for more guidance !
$\newline$  
$\newline$ 

#### Make.
--------------
- Now that you have `chocolatey` installed, we can install `make` by running the command : 
>```
> choco install make --version=3.81
>```
>
>
Once `make` installation is done , and assuming that you have downloaded the project files in your local machine it's very easy to workout everything. 
>
>$\newline$
>$\newline$
- To create the conda environemnt run the command : 
> 
> ```	
>	- $ make create_environment
> ```
>$\newline$
>$\newline$
- To setup the project run the command : 
> 
> ```	
>	- $ make setup
> ```
$\newline$
$\newline$

----
## Testing units.
----
### Testing the environment.

>
- To test packages and dependencies just run the command : 
> 
> ```	
>	- $ make env_test
> ```

Behind the scenes, make will go over the <em><strong>`Makefile`</em></strong> located in our directory which itself will chain to all test units located in <em><strong>`/src/tests`</em></strong> directory and do the heavy work for you.
>
>
### Testing syntax & style.
- To lint code scripts we are using flake8, just run the following command : 
> 
> ```	
>	- $ make lint
> ```

Under the hood, make will go over the <em><strong>`Makefile`</em></strong> located in our directory which itself will chain to all coding resources in <em><strong>`/src/functions`</em></strong> and <em><strong>`/notebooks`</em></strong> directories and will check the syntax and style of your code using flake8 to meet PEP8 standards.
>
>
### Testing internal modules.

>In our code we ended up using three main functions which help us to implemente the problem, the first function is called FuelCon it is used to calculate based on a linear model the fuel comsumption of the genset for a specific power load P. The second function is called `lwd, is the abreviation of load window, which is used to constructe a load profile for a specific number of time steps out of a given sets of power loads arrays. The third one is called lixtr and it's the abreviation of list extraction, which could be used in the section 'Pre-processing visualization data' for extracting lists out of dictionaries. So in order to make sure those functions are behaving as is should be some testing routings are required by following the next commands.

- To test the `FuelCon` function, run the command:  

```	
	 - $ make fuelCon_test
```

- To test the `lwd` function, run the command: 

```	
	 - $ make lwd_test
```

- To test the `lixtr` functions, run the command: 

```	
    - $ make lixtr_test
```