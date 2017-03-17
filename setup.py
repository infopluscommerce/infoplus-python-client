# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "Infoplus"
VERSION = "beta"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Infoplus API",
    author_email="api@infopluscommerce.com",
    url="http://www.infopluscommerce.com",
    keywords=["Swagger", "Infoplus API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Infoplus API.
    """
)


