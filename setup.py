# read the contents of your README file
from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lyrics-displayer',
    version='0.2',
    description='Displays lyrics of songs played on Sonos system.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='sonos lyrics lyricfetch',
    url='http://github.com/alpha1d3d/lyrics-displayer',
    author='Jonathan Loo',
    author_email='alpha1d3d@hotmail.com',
    license='MIT',
    packages=[
        'lyrics-displayer',
    ],
    zip_safe=False,
    scripts=['bin/sing-along'],
    install_requires=[
        'soco',
        'lyricfetch',
        'python-magic-bin',
    ]
)
