from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyspeechkit',
    version='1.0.0',
    author='Master',
    author_email='',
    description='Library for working with a range of technologies for speech recognition and synthesis from Yandex (Speechkit).',
    license='MIT',
    keywords='',
    url='https://github.com/pystorage/pyspeechkit',
    packages=['pyspeechkit'],
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
