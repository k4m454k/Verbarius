import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="verbarius",
    version="0.3",
    author="Vadim Apenko",
    author_email="k4m454k@gmail.com",
    description="VerbariusRus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k4m454k/VerbariusRus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
