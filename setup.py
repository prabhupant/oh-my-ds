from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ohmyds",
    version="0.0.2",
    author="Prabhu Pant",
    author_email="prabhupant09@gmail.com",
    description="Python library to visualize data strcutures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prabhupant/oh-my-ds",
    project_urls={
        "Bug Tracker": "https://github.com/prabhupant/oh-my-ds/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("tests",)),
    #include_package_data=True,
    python_requires=">=3.6",
    keywords=[
        'data structures', 
        'tree', 
        'graph', 
        'linked list', 
        'stack', 
        'queue', 
        'education', 
        'visualization'
    ]
)
