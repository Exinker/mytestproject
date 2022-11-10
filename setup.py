
from setuptools import setup, find_packages


setup(
    name='mytestproject',
    description='My easy test project',
    license='MIT',

    version='0.0.1',

    author='Pavel Vashchenko',
    author_email='exinker@gmail.com',

    packages=find_packages('./mytestproject/'),
    # package_dir={
    #     '': './/',
    # },
    # package_data={
    #     '': [],
    # },

    # requires=[],

)


