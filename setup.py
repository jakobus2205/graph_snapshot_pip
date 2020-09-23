import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graph-snapshot-NicoHaaf", # Replace with your own username
    version="0.0.1",
    author="Josua Kugler, Nico Haaf",
    author_email="josua.kugler@stud.uni-heidelberg.de, nico.haaf@stud.uni-heidelberg.de",
    description="A small package for creating snapshots of graphs with networkx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
)