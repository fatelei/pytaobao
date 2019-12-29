# -*- coding: utf8 -*-

from setuptools import find_packages, setup

setup(
    name='pytaobao',
    version='0.0.1',
    license='PRIVATE',
    author='fatelei',
    author_email='fatelei@gmail.com',
    url='https://github.com/fatelei/pytaobao',
    description='voom backend',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
)
