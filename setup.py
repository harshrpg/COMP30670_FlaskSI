from setuptools import setup, find_packages

setup(
    version=0.1,
    name='systeminfo_flask',
    packages=['app'],
    include_package_data=True,
    dependency_links=[
        'https://github.com/harshrpg/COMP30670_CookieCutter.git@master#egg=systeminfo-0.1'],
    install_requires=['flask','systeminfo']
)
