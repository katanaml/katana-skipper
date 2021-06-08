"""Setup script for katana-skipper"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="katana-skipper",
    version="1.0.0",
    description="Helper library to simplify RabbitMQ for microservices",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/katanaml/katana-skipper",
    author="Andrej Baranovskij",
    author_email="abaranovskis@redsamuraiconsulting.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["eventhandler"],
    include_package_data=False,
    install_requires=[
        "pika"
    ],
    entry_points={"console_scripts": ["katanaskipper=eventhandler.__main__:main"]},
)
