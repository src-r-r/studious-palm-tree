#!/usr/bin/env python3

from setuptools import (
    setup,
    find_packages,
)

setup(
        name="setuptools_example",
        version="0.1",
        packages=find_packages(),
        include_package_data=True,
    )
