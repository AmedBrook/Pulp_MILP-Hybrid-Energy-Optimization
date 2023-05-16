## How to contribute to HEO model.
---

This is a guide on how to contribute to HEO project.

#### Contribution steps

1. Fork the repo.

2. Clone your forked repo.

3. Install dependencies.

4. Make your changes.

5. Create a test for your changes if needed.

6. Make sure all the tests pass.

7. Lint the code.

8. Ensure the docs are accurate.

9. Submit a Pull Request.

On top of having python installed, we will be using git and the command line. Also, we assume you have a github account and know how to fork a project. We will use plain git through the command line but feel free to use the git client of your choice.

### Forking the project
You can follow the github guides to fork a project: [here](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) and also [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

You need a github account to fork a github project. It’s free.

### Cloning the project
You first need to download the HEO project from your fork. In the following command replace ``usrn`` with your actual username:

```
$ git clone git@github.com:usrn/Pulp_MILP-Hybrid-Energy-Optimization.git
```
That’s it, you will download the whole project.


### Running tests
To run the project tests you need to execute the Makefile rules:

```
$ cd Pulp_MILP-Hybrid-Energy-Optimization/Makefile
$ make
```
It will test your python environment, PuLP packages, internal modules as well as installing the required external dependancies if they are not already installed.

### Creating a test file
When you fix an issue in HEO model or add a functionality, you should add a test to the repository. For this you should do the following: 

 - Go to src/functions/ folder and add a new method.
 - Go to src/functions/tests folder and add an other method that tests your changes.

### linting the code
After writing the code nedded for the contribution you have to check for style and syntax errors, for this we use flake8, you just run the command in root directory : 

```
$ make lint
```


### Building the documentation
The documentation is based on Mkdocs and MathJax. 
To build the documentation see the Readme file (Sections Mkdocs and Mathjax). 

### Making a Pull Request
When you’re done with the changes in your machine and you’re satisfied with the result you have, you can commit it, push it to github and then create a PR. The first two are easy:

```
$ git status # this shows what's changed
$ git add some_modified_file.py # do this for all changes you want to write
$ git commit -m "some message" # include a meaningful message
$ git push main
```