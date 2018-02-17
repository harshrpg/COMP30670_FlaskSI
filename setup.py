from setuptools import setup, find_packages

setup(
    version=0.1,
    name='systeminfo_flask',
    packages=['app'],
    include_package_data=True,
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'getPlatformInfo=app.run:main']})

