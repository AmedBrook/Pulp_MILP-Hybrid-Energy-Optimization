import setuptools
from setuptools import setup, find_namespace_packages

def get_install_requirements():    

    with open("requirements.txt", "r", encoding="utf-8") as f:        
        reqs = [x.strip() for x in f.read().splitlines()]    
        reqs = [x for x in reqs if not x.startswith("#")]    
    return reqs

def get_long_description():

    # I want my readme to be part of the setup, so let's read it.
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description
    

setup(

    name='HYH',
    version='0.1.0',
    authors='Novia Intelligent Systems Institute',
    maintainer='Ahmed Mabrouk', 
    description='MILP Hybrid Energy Optimization',
    long_description= get_long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization',
    maintainer_email='Ahmed.Mabrouk@novia.fi',
    license='MIT',
    # additional classifiers that give some characteristics about the package.
    classifiers=[

            # it's still early stages.
           'Development Status :: 3 - Alpha',

            # Our Intended audience is mostly those who understand Energy Optimization and Integration.
           'Intended Audience :: Energy Optimization and Integration',

           # Our License is MIT.
           'License :: OSI Approved :: MIT License',

           # We wrote the user in English
           'Natural Language :: English',

           # The user should work on all OS.
           'Operating System :: OS Independent',

           # The user is intendend for PYTHON 3
           'Programming Language :: Python :: 3'
      ],
    packages=setuptools.find_namespace_packages(include=['src', 'src.functions', 'src.tests'] ),
    install_requires= get_install_requirements()
    )

