import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="test_cdk_py",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "test_cdk_py"},
    packages=setuptools.find_packages(where="test_cdk_py"),

    install_requires=[
        "aws-cdk.core==1.111.0",
        "aws-cdk.assertions==1.111.0",
        "aws-cdk.aws-s3==1.111.0",
        "pytest"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
