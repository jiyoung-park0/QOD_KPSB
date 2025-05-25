# setup.py
from setuptools import setup, find_packages

setup(
    name="qodkpsb",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "qod_kpsb": ["model/*"]
    },
    install_requires=[
        "torch>=1.12.0",
        "transformers>=4.0.0"
    ],
    author="Jiyoung Park",
    description="Korean Political Sentiment Classifier based on KoELECTRA",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7",
)
