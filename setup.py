from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> list[str]:
    '''
    this function returns the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
        
setup(
    name='ml-project',
    version='0.0.1',
    author='Chirag',
    author_email='chiragbansal517@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)