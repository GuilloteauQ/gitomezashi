from setuptools import setup

setup(
    # Application name:
    name="gitomezashi",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Quentin Guilloteau",
    author_email="Quentin.Guilloteau@inria.fr",

    # Packages
    packages=["app"],

    # Include additional files into the package
    # include_package_data=True,
    entry_points={
        'console_scripts': ['gitomezashi=app.gitomezashi:main'],
    },

    #
    # license="LICENSE.txt",
    description="Hitomezashi Stitch Patterns for git commit hashes",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "GitPython",
        "svgwrite",
        "cairosvg"
    ]
)
