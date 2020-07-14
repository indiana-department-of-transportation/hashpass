import os.path
import setuptools
import subprocess

with open("README.md") as f:
    long_description = f.read()

version = subprocess.check_output([
    "git",
    "--git-dir",
    os.path.join(os.path.dirname(__file__), ".git"),
    "tag"
]).decode("utf-8").strip().split("\n")[-1]

current_dir = os.path.dirname(os.path.realpath(__file__))

url = subprocess.check_output([
    "git",
    "--git-dir",
    os.path.join(os.path.dirname(__file__), ".git"),
    "config",
    "--get",
    "remote.origin.url"
]).decode("utf-8").strip()

setuptools.setup(
    name="hashpass",
    version=version,
    author="jasmith79",
    author_email="jasmith79@gmail.com",
    description="Hashes passwords for use in ansible playbooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=["hashpass"],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    entry_points={
        "console_scripts": [
            "hashpass = hashpass.gen_pass_sha:main"
        ]
    }
)
