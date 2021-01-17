import setuptools

from jiral.version import VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jiral",
    version=VERSION,
    author="ash84",
    author_email="sh84.ahn@gmail.com",
    description="simple cli for jira",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AhnSeongHyun/jiral",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["jiral=jiral.__main__:app"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
