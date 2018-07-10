import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='RFSG_bootcamp',
    version='0.0.1',
    author='Roberto Felipe SG',
    author_email='robertofelipe.sg@gmail.com',
    description='Utilities for use in bootcamp.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
