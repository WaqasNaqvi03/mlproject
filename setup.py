from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    
    '''
    This function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() ## readlines when reading reads \n when line is changed. to remove that we will use replace function
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements



setup(
name = 'MLproject',
version = '0.0.1',
author = "Waqas",
author_email ="engineerwaqas1@hotmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt") 
## install_requires = ['pandas','numpy','seaborn'] Since we may require many many packages we cannot write each end every one, 
##rather we create a function and give a path of the file and get our packgs req from file (in our case requirments.txt file)

)