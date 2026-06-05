from setuptools import setup, find_packages
from os import path
from importlib.metadata import distribution, PackageNotFoundError

with open("README.md", "r") as file:
    long_description = file.read()

_dir = path.dirname(__file__)


def is_installed(pkgname):
    try:
        distribution(pkgname)
        return True
    except PackageNotFoundError:
        return False


dependencies = [
    "numpy>=1.17.0",
    "numba>=0.47.0",
    "scikit-image>=0.17.1",
    "scipy>=1.6.3",
    "tqdm>=4.50.0"
]

# Only pull in a CuPy wheel if the environment doesn't already provide one.
# The list includes modern CUDA 12.x / 13.x wheel names and the generic
# 'cupy' package so a conda/pip-provided CuPy is correctly detected and we
# don't accidentally install a second, conflicting CuPy build.
_cupy_packages = (
    "cupy", "cupy-cuda13x", "cupy-cuda12x",
    "cupy-cuda102", "cupy-cuda110", "cupy-cuda111", "cupy-cuda112",
    "cupy-cuda113", "cupy-cuda114", "cupy-cuda115", "cupy-cuda116",
)
if not any(is_installed(pkg) for pkg in _cupy_packages):
    dependencies.append("cupy-cuda13x>=13.6.0")

setup(
    name='opticalflow3d',
    version="0.3.2",
    description='GPU/CUDA optimized implementation of 3D optical flow algorithms such as Farneback two frame motion estimation and Lucas Kanade dense optical flow algorithms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=dependencies,
    author='Xianbin Yong',
    author_email='xianbin.yong13@sps.nus.edu.sg',
    url='https://gitlab.com/xianbin.yong13/opticalflow3d',
    packages=find_packages(),
    license="GPLv3",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering",
    ],
    python_requires='>=3.7',
    project_urls={
        'Research group': 'https://ctlimlab.org/',
        'Source': 'https://gitlab.com/xianbin.yong13/opticalflow3d',
    },
)
