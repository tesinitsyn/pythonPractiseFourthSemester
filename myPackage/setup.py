from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    description='My sample package',
    author='John Doe',
    author_email='john.doe@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
)