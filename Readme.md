## HEO.
---

PuLP-MILP based Hybrid Energy Optimization, for fuel minimization: MILP model with semi-continuous power supply and battery logic.



## Project description and context. 
---


The project aims to explore the possibility of integrating 
energy storage faciltities within the shipping industry marcket. 
In this application we simulate one possible solution on how to
synchronize fuel based gensets with a battery storage system
alonge side with energy optimization to reduce energy cost throughout the trip journey. The whole project is build based on an optimization mathimatical model and uses MILP (mixed intiger linrear programing) methodes to solve optimaly the problem.  

In the Notebook scripts associated with this porject, we simulate an application used to optimize fuel consumption for vessels using one genset to produce the required energy and one battery storage system to store and realese the excess of that energy when needed in a hybrid mode.

The framwork used in this case study is PuLP, to solve a Mixed Intger Linear Programming problem together with first the built-in solver CBC and then with a commercial solver, we used Gurobi in our case.

## Project use case.
---

this particular case is initially specefic for the offshore shipping industry as they are the most transportation fuel consuming and needing some sort of solutions to use fuel  optimally in their trips. However this is not only exlusive to this sector, it can be easily extended to other sectors as long as the purpose is to optimize energy usage and energy hybridization.


## Project setup options. 
---
Due to everyone's preferences and environments, we have provided two differente ways to setup the project with the required external dpendencies and internal modules. 

###  Standalone setup.
---
>
$\newline$  
In order to setup the project environment and install all packages and dependencies, run the commands :
>
>```
>   - $ conda create -n heo python
>   - $ conda activate heo
>   - $ pip install -e .
>```


### Pre-configured setup.
---


While the manual installation can walk you through around the various commands basics for each used packages in the project, chances are you might already know those commands and you don't want to bother yourself about taping every single command, so that's why we have provided the possibility to use <em><strong>`make`</em></strong> scripting, to make life easy for you. You find in the following the commands you will need to do this. 


In case you have make installed in your system, for Linux based system it comes already installed in your system you don't need to install anything just skeep this part to {...}. For windows based systems there are multiple ways to get GNU make installed, like for example Cygwin, Nmake, Cmake..., however we recommand to go for [chocolatey](https://community.chocolatey.org/packages/make), we think it's the most straighforward way to install make for windows systems with less effort. 
$\newline$  
$\newline$  

#### chocolatey.


>
First thing first, we will install chocolatey, make sure you are using the Powershell command as an admin,
>	
- Then run this command first :
>```
> Get-ExecutionPolicy 
>```
- If it returns Restricted, then run : 
>```
> Set-ExecutionPolicy AllSigned or Set-ExecutionPolicy Bypass -Scope Process
>```
Now, to install `chocolatey` run the following command by coping it at once and past it in command line, then hit enter:
>
>```
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
>```
>
Please check [chocolatey](https://community.chocolatey.org/packages/make) website for more guidance !
$\newline$  
$\newline$ 

#### Make.

Now that you have `chocolatey` installed, we can install `make` by running the command : 
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
>


## Test units.
---
Testing code is important to garantee consistency and availabality of this project. Test units are devide in three main aspects: testing Pulp modler which test the appropriate solvers, testing code syntax and style conferming to PEP8 standard, testing internal modules which are mainly functions used for implemeting the problem. 

#### Pulp & environment testing.
----------------------------
- To test Python environment along side with the required Pulp pakages you will need just to run the command : 
> 
> ```	
>	- $ make env_test
> ```

Behind the scenes, make will go over the <em><strong>`Makefile`</em></strong> located in our directory which itself will chain to all test units located in <em><strong>`/src/tests`</em></strong> directory and do the heavy work for you.
>
>
#### Testing syntax & style.
----------------------------
- To lint code scripts we are using flake8, just run the following command : 
> 
> ```	
>	- $ make lint
> ```

Under the hood, make will go over the <em><strong>`Makefile`</em></strong> located in our directory which itself will chain to all coding resources in <em><strong>`/src/functions`</em></strong> and <em><strong>`/notebooks`</em></strong> directories and will check the syntax and style of your code using flake8 to meet PEP8 standards.
>
>
#### Testing internal modules.
-----------------------------

- To test the `FuelCon` function, run the command:  
>
>```	
>	 - $ make fuelCon_test
>```

- To test the `lwd` function, run the command: 
>
>```	
>	 - $ make lwd_test
>```

- To test the `lixtr` functions, run the command: 
>
>```	
>    - $ make lixtr_test
>```

In our code we ended up using three main functions which help us to implemente the problem, they are located under <strong><em>`src/functions`</em></strong> directory. 

The first function is called <strong><em>`FuelCon`</em></strong> it is used to calculate based on a linear model the fuel comsumption of the genset for a specific power load P.
 The second function is called <strong><em>`lwd`</em></strong>, is the abreviation of load window, which is used to constructe a load profile for a specific number of time steps out of a given sets of power loads arrays. 
 The third one is called <strong><em>`lixtr`</em></strong> and it's the abreviation of list extraction, which could be used in the section 'Pre-processing visualization data' for extracting lists out of dictionaries. So in order to make sure those functions are behaving as is should be some testing routings are required by following the next commands.