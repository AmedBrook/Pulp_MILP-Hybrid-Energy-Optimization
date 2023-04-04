## HEO.
----

PuLP-MILP based Hybrid Energy Optimization, for fuel minimization: MILP model with semi-continuous power supply and battery logic.

## Project description and context
----
The project aims to explore the possibility of integrating energy storage facilities within the shipping industry market. In this application we simulate one possible solution on how to synchronize fuel based gensets with a battery storage system alongside with energy optimization to reduce energy cost throughout the trip journey. The whole project is build based on an optimization mathematical model and uses MILP (mixed integer linear programming) methods to solve optimally the problem.

In the Notebook scripts associated with this project, we simulate an application used to optimize fuel consumption for vessels using one genset to produce the required energy and one battery storage system to store and realise the excess of that energy when needed in a hybrid mode.

The farmwork used in this case study is PuLP, to solve a Mixed Integer Linear Programming problem together with first the built-in solver CBC and then with a commercial solver, we used Gurobi in our case.

## Project use case
----
This particular case is initially specific for the offshore shipping industry as they are the most transportation fuel consuming and needing some sort of solutions to use fuel optimally in their trips. However, this is not only exclusive to this sector, it can be easily extended to other sectors as long as the purpose is to optimize energy usage and energy hybridization.

## Project setup options

----

### Standalone setup
###### Environment

* Create a new environment aside of the root, and name it somthing recognisable, we gave it a name here as HEO_model, we have used here python version 3.9.7. 

To do so, run the command : `$ conda create --HEO_model python=3.9.7`

###### Requirements and Dependencies
 Before stating the setup process you need to have <em>`setuptools`</em> installed, if you don't have it already do through the following commands:

* Python package index (Pypi) : `$ pip install setuptools`

* Anaconda package index (Conda) : `$ conda install -c conda-forge setuptools`

 Now that you have <em>`setuptools`</em> in you environment, in order to install all packages and dependencies at once run the command : 

*  `$ python -m pip install -e .`

### Pre-configured setup
----
While the manual installation can walk you through around the various commands basics for each used packages in the project, chances are you might already know those commands and you don't want to bother yourself about taping every single command, so that's why we have provided the possibility to use `make` scripting, to make life easy for you. You find in the following the commands you will need to do this. 


In case you have make installed in your system, for Linux based system it comes already installed in your system you don't need to install anything just skeep this part to {...}. For windows based systems there are multiple ways to get GNU make installed, like for example Cygwin, Nmake, Cmake..., however we recommand to go for [chocolatey](https://community.chocolatey.org/packages/make), we think it's the most straighforward way to install make for windows systems with less effort. 

##### chocolatey
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
    

##### Make
* Now that you have `chocolatey` installed, we can install `make` by running the command : 

``` 
     $ choco install make --version=3.81
```

Once make installation is done, and assuming that you have downloaded the project files in your local machine it's very easy to workout everything. 

* To create the conda environment run the command : 
 
```	
	 $ make create_env
```

* To setup the project run the command : 

``` 
	 $ make setup
```
#### Mkdocs.

We are using Mkdocs in order to generate documentation pages for the project.

to install Mkdocs, run the command : 
```
   - $ pip install mkdocs
```

To create a new project with the name ´heo´, you can run: 
```
   - $ mkdocs new heo
```

After creation the project, you might have something simmilar to this: 

```
            mkdocs.yml
      		docs
		      |___ index.md
                    |___./...
```									

if you want to preview live the changes you make on the mkdocs pages, then you can serve them by running the command: 
```
   - $ python mkdocs serve
```

##### Mathjax
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

## Testing units
-------------------------

#### Testing the environment
* To test packages and dependencies just run the command : 

```	
	- $ make env_test
```
Behind the scenes, make will go over the `Makefile` located in our directory which itself will chain to all test units located in `/src/tests` directory and execute every single test module existing in that directory.

----

#### Testing syntax & style
* To lint code scripts we are using flake8, just run the following command : 

```	
	 - $ make lint
```
Under the hood, make will go over the `Makefile` located in our directory which itself will chain to all coding resources in `/src/functions` and `/notebooks` directories and will check the syntax and style of your code using flake8 to meet PEP8 standards.


#### Testing internal modules
In our code we ended up using three main functions which help us to implemente the problem, the first function is called `FuelCon` it is used to calculate based on a linear model the fuel comsumption of the genset for a specific power load `P`. The second function is called `lwd`, is the abreviation of load window, which is used to constructe a load profile for a specific number of time steps out of a given sets of power loads arrays. The third one is called `lixtr` and it's the abreviation of list extraction, which could be used in the section 'Pre-processing visualization data' for extracting lists out of dictionaries. So in order to make sure those functions are behaving as is should be some testing routings are required by following the next commands. 

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

