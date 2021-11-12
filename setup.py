from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
  readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
  name = "Python Starting Project",
  version = "0.0.1",
  author = "Henry Chou",
  author_email = "hendry.js1247@gmail.com",
  description = "A template for setup basic python project",
  long_description = readme,
  long_description_content_type = "text/markdown",
  url = "https://github.com/Hendryboyz/python-project-setup",
  packages = find_packages(),
  install_requires = requirements,
  classififiers = [
    "Programming Language :: Puython :: 3.9"
  ]
)
