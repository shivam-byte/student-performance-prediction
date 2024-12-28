from setuptools import find_packages,setup
from typing import List

hyphon = '-e .'
def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace('\n','') for req in requirements]


        if hyphon in requirements:
            requirements.remove(hyphon)
    
    return requirements




setup(
    name = 'student performance prediction project',
    version = '0.0.1',
    author = 'shivam',
    author_email = 'shivam4806@gmail.com',
    packages = find_packages(), 
    install_requires = get_requirements('requirements.txt')

)
