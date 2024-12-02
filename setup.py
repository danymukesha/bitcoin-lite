from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("src/bitcoin_lite/transaction.pyx"),
    package_dir={"": "src"},
)
