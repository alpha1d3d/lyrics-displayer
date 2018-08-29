from setuptools import setup

setup(
    name='lyrics-displayer',
    version='0.1',
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
        'lyrics-displayer.lyrics',
        'lyrics-displayer.players',
    ],
    zip_safe=False,
    scripts=['bin/sing-along'],
    install_requires=[
        'requests',
        'html2text',
        'soco',
        'PyLyrics',
    ]
)
