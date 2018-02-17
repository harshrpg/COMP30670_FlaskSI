from setuptools import setup, find_packages

setup(
    name='systeminfo_flask',
    packages=['app'],
    include_package_data=True,
    install_requires=['flask'],
    dependency_links=[
        'git+https://github.com/harshrpg/COMP30670_CookieCutter.git@master#egg=sysinfo-0.1'],
    enrty_points='''
        [flask.commands]
        run_app=run:main
    '''
)
