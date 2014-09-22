
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-hiera",
    version = "0.0.1",
    author = "Mike Rochford",
    author_email = "mike@mikerochford.com",
    description = (""),
    keywords = "",
    url = "",
    packages=find_packages(),
    long_description=read('README.md'),
)
