from setuptools import find_packages, setup


install_requires = ["ruff"]

setup(
    name="poc_style_bot",
    version="0.1.0",
    author="Sayak Paul",
    author_email="spsayakpaul@gmail.com",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=list(install_requires),
    package_data={"poc_style_bot": ["py.typed"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
