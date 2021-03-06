import os
from setuptools import setup, Extension, find_packages

module = Extension('_synther', sources=['src/lib.cpp', 'src/WavIO.cpp'])

setup(
  name='synther', 
  ext_modules = [module], 
  py_modules=['synther'], 
  package_dir={'':'src'},)
