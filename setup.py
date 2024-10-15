from setuptools import setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name = "scalable-app-prototype",
    description="coso",
    author="marce",
    author_email="marceloantezana70@gmail.com",
    long_description=readme,
    test_suite="clothes_shop/test"
)