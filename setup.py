import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED = [
    'numpy',
    'pandas',
]

setuptools.setup(
    name="dfunc-MaxTechniche",
    version="0.0.2",
    author="MaxTechniche",
    author_email="max.techniche@gmail.com",
    description="Multiuse functions to clean pandas DataFrames",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaxTechniche/lambdata-MaxTechniche",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    python_requires='>=3.6',
)
