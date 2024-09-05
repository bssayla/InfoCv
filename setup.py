from setuptools import find_packages, setup

setup(
    name="InfoCV",
    version="0.1",
    author="Ouaicha Mohamed",
    author_email="Ouaicha47@gmail.com",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=[
        "pytest",
        "setuptools",
        "streamlit",
        "pypdf",
        "docx",
    ],
)
