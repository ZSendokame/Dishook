from setuptools import setup, find_packages

readme = open('README.md')

setup(
    name='dishook',
    version='1.0.4',
    author='Sendokame',
    url='https://github.com/ZSendokame/Dishook',
    description='Control your discord webhooks on a nice way.',
    long_description_content_type='text/markdown',
    long_description=readme.read(),
    packages=(find_packages(include=['dishook']))
)
