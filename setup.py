from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirement_lst: List[str] = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print(f"{file_path} not found")
        
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Utkarsh',
    author_email='utkarsh.vishu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
