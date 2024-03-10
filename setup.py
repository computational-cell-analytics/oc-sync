import runpy
from setuptools import setup, find_packages

__version__ = runpy.run_path("oc_sync/__version__.py")["__version__"]

requires = ["pyocclient"]

setup(
    name="oc_sync",
    packages=find_packages(exclude=["test"]),
    version=__version__,
    author="Constantin Pape",
    install_requires=requires,
    url="https://github.com/computational-cell-analytics/oc-sync",
    license="MIT",
    # entry_points={
    #     "console_scripts": [
    #         "view_container = elf.visualisation.view_container:main",
    #     ]
    # },
)
