from setuptools import setup, find_packages

def get_install_requirements():    

    """    It reads the requirements.txt file and returns a list of all the requirements    
           :return: A list of all the requirements for the project.    
    """    
    with open("requirements.txt", "r", encoding="utf-8") as f:        
        reqs = [x.strip() for x in f.read().splitlines()]    
        reqs = [x for x in reqs if not x.startswith("#")]    
        return reqs
    
setup(
    
    name='HYH',
    version='0.1.0',
    authors='',
    maintainer='Ahmed Mabrouk', 
    description='MILP Hybrid Energy Optimization',
    url='https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization',
    maintainer_email='Ahmed.Mabrouk@novia.fi',
    license='MIT',
    packages=setuptools.find_packages(include=['HYH']),
    install_requires=get_install_requirements()
    ]
)

