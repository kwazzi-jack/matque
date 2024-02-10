import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", "r") as file:
    requirements = file.readlines()

setuptools.setup(
    name="matque",
    version="0.0.1",
    author="Brian Welman",
    author_email="brianallisterwelman@gmail.com",
    description="Library to generate mathematics questions for "
    + "various topics with solutions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brianwelman2/matque.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GPL License",
        "Operating System :: Unix",
    ],
    python_requires=">=3.10",
    test_suite="tests",
    install_requires=requirements,
    include_package_data=True,
)
