from setuptools import setup, find_packages 

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

setup(
    name="src",
    version="0.0.1",
    author="vikas",
    description="a small package for dvc ml use case",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    uri="https://github.com/vikasyetinthala/dvcmlproject.git",
    author_email="vikasyetintala07@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)