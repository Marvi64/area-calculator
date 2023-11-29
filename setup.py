from setuptools import setup, find_packages

setup(
    name="area_calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    python_requires=">=3.6",
)
