from setuptools import setup, find_packages

setup(
    name='systeminfo_flask',
    packages=['app'],
    include_package_data=True,
    install_requires=['flask'],
    dependency_links=[
        'https://github.com/harshrpg/COMP30670_CookieCutter/tarball/master#egg=systeminfo-0.1']
)
