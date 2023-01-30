# PuLP-MILP Hybrid Energy Optimization. 

For full project materials visit [https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization](https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization).


## Commands:



##### Project's environment.

* `$ conda create --HYH_model python=3.9.7` - Create a new environment aside of the root, and name it somthing recognisable, we named here as HYH_model, we have used here python version 3.9.7. to do so you tape.


##### PuLP installation.

* `$ conda install -c forge-pulp` - We use the command in order to install Pulp modler packages.
* `$ conda search -c forge-pulp` - You can search for Pulp packages after installation.
* `$ conda list` - Then you can list Pulp packages afetrwards.


##### Gurobi installation.

* `$ conda install -c gurobi gurobi` - To install Gurobi solver packages, we use this command.
* `$ conda search -c gurobi gurobi` - You can search for Pulp packages after installation.
* `$ conda list` - Then you can list Pulp packages afetrwards.



## Project layout.



    
    data/
        exteranl/
        interinm/
        processed/
        raw/
        .gitkeep
    docs/
        commands.rst
        conf.py
        getting-started.rst
        index.rst
        make.bat
        ...
    mkdocs/
        docs/
        site/
    models/
        .gitkeep
    notebooks/
        tests/
            .gitkeep
            HYH_V0.2.0.ipynb
        HYH_V0.1.4.ipynb
        HYH_V0.1.5.ipynb
        HYH_V0.2.1.ipynb
    references/
        .gitkeep
    reports/
        figures/
        Load Analysis & Benchmark/
        ...
    src/
        dataset/
        functions/
            tests/
                fuel_consumption_tests.py
                list_extraction_tests.py
                load_window_tests.py
        __init__.py
        .gitkeep
        dictionaries_add.py
        fuel_consumption.py
        list_extraction.py
        load_window.py
        rand_val.py
        rand_window.py
    .env
    .gitignore
    Authors.txt
    Changelog.md
    Gurobi-license.txt
    License
    Makefile
    Readme.md
    Requirements.txt
    setup.py
    test_environment.py
    tox.ini
    

        
    