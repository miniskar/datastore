import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datastore-ayoung48",
    version="0.0.1",
    author="Aaron Young",
    author_email="ayoung48@vols.utk.edu",
    description="Useful datastore.",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/Geekdude/bunch/src/master/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
    install_requires=[
        'json_tricks',
    ],
)
