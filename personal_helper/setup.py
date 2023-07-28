from setuptools import find_namespace_packages, setup

setup(
    name='Personalhelper',
    version='1.0',
    packages=find_namespace_packages(),
    install_requires=["prettytable"],
    entry_points={"console_scripts": ["personal_helper=personal_helper.personal_helper:main"]}
)
