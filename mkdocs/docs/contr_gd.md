# How to contribute to HYH model.

This is a guide on how to contrubute to HYH.

#### Contribution steps :

1. Fork the repo.

2. Clone your forked repo.

3. Install dependencies.

4. Make your changes.

5. Create a test for your changes if needed.

6. Make sure all the tests pass.

7. Ensure the docs are accurate.

8. Submit a Pull Request.

On top of having python installed, we will be using git and the command line. Also, we assume you have a github account and know how to fork a project. We will use plain git through the command line but feel free to use the git client of your choice.

### Forking HYH.
You can follow the github guides to fork a project: [here](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) and also [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

You need a github account to fork a github project. It’s free.

### Cloning the project. 
You first need to download the HYH project from your fork. In the following command replace ``usrn`` with your actual username:

```
$ git clone git@github.com:usrn/Pulp_MILP-Hybrid-Energy-Optimization.git
```
That’s it, you will download the whole project.


### Running tests.
To run tests of HYH you need to run the Makefile:

```
$ cd Pulp_MILP-Hybrid-Energy-Optimization/Makefile
$ make
```
It will test your python environment and the PuLP packages as well as installing the required dependancies if not already installed.

### Creating a test.
When you fix an issue in pulp or add a functionality, you should add a test to the repository. For this you should do the following: 

 - Go to src/functions/ folder and add a new method.
 - Go to src/functions/tests folder and add an other method that tests your changes.


### Building the documentation.
The documentation is based in Mkdocs and MathJax.

To build the documentation see the Readme file (sections mmkdocs and Mathjax). 

### Making a Pull Request.
When you’re done with the changes in your machine and you’re satisfied with the result you have, you can commit it, push it to github and then create a PR. The first two are easy:

```
$ git status # this shows what's changed
$ git add some_modified_file.py # do this for all changes you want to write
$ git commit -m "some message" # include a meaningful message
$ git push main
```