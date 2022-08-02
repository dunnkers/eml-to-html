#!/usr/bin/env python

from setuptools import find_namespace_packages, find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="eml-to-html",
        version="0.0.2",
        py_modules=["eml_to_html"],
        scripts=["eml_to_html.py"],
        entry_points={"console_scripts": ["eml-to-html = eml_to_html:main"]},
        description="Converts `.eml` files to HTML.",
        keywords="",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        license="MIT",
        license_file="LICENSE",
        author="Jeroen Overschie",
        author_email="jeroen@darius.nl",
        maintainer="Jeroen Overschie",
        maintainer_email="jeroen@darius.nl",
        url="https://github.com/dunnkers/eml-to-html",
        project_urls={
            "Github": "https://github.com/dunnkers/eml-to-html",
            "Bug Tracker": "https://github.com/dunnkers/eml-to-html/issues",
            "Documentation": "https://dunnkers.com/eml-to-html",
        },
        include_package_data=True,
        install_requires=[],
        python_requires=">= 3.7",
        setup_requires=["black==21.12b0", "pytest-runner>=5"],
        tests_require=["pytest>=6", "pytest-cov>=3", "pytest-dependency"],
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS",
            "Operating System :: Microsoft :: Windows",
            "Typing :: Typed",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
