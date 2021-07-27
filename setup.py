from setuptools import find_packages, setup


def read(filename=None):
    return [i.strip() for i in open(filename).readlines()]


setup(
    name="myapp",
    version="0.1.0",
    description="Este é o Myapp",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
    entry_points="""
        [console_scripts]
        myapp=cli.cli:cli
    """,
)
