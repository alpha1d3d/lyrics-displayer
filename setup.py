from setuptools import setup

setup(
    name='lyrics-displayer',
    version='0.2',
    description='Displays lyrics of songs played on Sonos system.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='funniest joke comedy flying circus',
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
