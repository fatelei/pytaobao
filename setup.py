# -*- coding: utf8 -*-

from setuptools import find_packages, setup
from pytaobao import __version__

setup(
    name='pytaobao',
    version=__version__,
    license='PRIVATE',
    author='fatelei',
    author_email='fatelei@gmail.com',
    url='https://github.com/fatelei/pytaobao',
    description='voom backend',
    packages=find_packages(where='.', exclude=['tests', 'scriptss']),
    zip_safe=False,
)
