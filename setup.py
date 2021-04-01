import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blackerz-wrapper", # Replace with your own username
    version="0.0.2",
    author="Fastering18",
    author_email="brahmana081@gmail.com",
    description="Developer kit to interact with our API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fastering18/Blackerz-Wrapper-Python",
    project_urls={
        "Bug Tracker": "https://github.com/Fastering18/Blackerz-SDK-Python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=2',
)
