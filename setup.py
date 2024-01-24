import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='final_project_01',
    version='4',
    author='Nelson Ramírez',
    author_email='jaguar1077@gmail.com',
    description='Proyecto final del curso de Configuración profesional de entornos de trabajo para ciencia de datos. Fecha: 13/01/2024.',
    python_requires='>=3',
    license='',
    url='',
    packages=find_packages(),
    long_description=readme(),
)