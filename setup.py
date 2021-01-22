from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="VERAS-Slanman3755",
    version="0.0.1",
    author="Spencer Lanman",
    author_email="slanman3755@gmail.com",
    description="Vatsim En Route Automation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slanman3755/VERAS",
    packages=find_packages(exclude='tests'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9, <4',
    install_requires=[
        'click>=7.1.2',
        'neo4j-driver>=4.2.1',
    ],
)