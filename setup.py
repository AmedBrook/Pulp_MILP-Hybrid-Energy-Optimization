from setuptools import setup, find_packages

setup(
    
    name='HYH',
    version='0.1.0',
    authors='Ahmed Mabrouk / Johan Westö / Ray Pörn',
    description='MILP Hybrid Energy Optimization ',
    url='https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization',
    author_email='Ahmed.Mabrouk@novia.fi',
    license='MIT',
    packages=find_packages(),
    install_requires=[ # those are the requirements for the project packages.
        'gurobipy==10.0.0'
        'PuLP==2.7.0'
        'matplotlib==3.2.2'
        'numpy==1.21.6' 
    ]
)
