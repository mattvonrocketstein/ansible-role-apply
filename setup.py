#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" setup.py for ymir
"""
import os
import sys
from setuptools import setup

# make sure that finding packages works, even
# when setup.py is invoked from outside this dir
this_dir = os.path.dirname(os.path.abspath(__file__))
if not os.getcwd() == this_dir:
    os.chdir(this_dir)

# make sure we can import the version number so that it doesn't have
# to be changed in two places. ymir/__init__.py is also free
# to import various requirements that haven't been installed yet
sys.path.append(os.path.join(this_dir, 'ansible_role_apply'))
from version import __version__  # flake8: noqa
sys.path.pop()

base_url = 'https://github.com/mattvonrocketstein/ansible-role-apply/'
setup(
    name='ansible-role-apply',
    version=__version__,
    description='',
    author='mattvonrocketstein',
    author_email='$author@gmail',
    url=base_url,
    download_url=base_url + '/tarball/master',
    packages=['ansible_role_apply'],
    keywords=['ansible', 'devops'],
    entry_points={
        'console_scripts':
        ['ansible-role-apply = ansible_role_apply.bin:entry', ]},
    install_requires=[
        'shellescape==3.4.1',
        "Fabric",
        'jinja2',
    ],
)