from setuptools import setup

setup(
    name='sonos_lyrics',
    version='0.1',
    description='Displays lyrics of songs played on Sonos system.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='funniest joke comedy flying circus',
    url='http://github.com/alpha1d3d/sonos_lyrics',
    author='Jonathan Loo',
    author_email='alpha1d3d@hotmail.com',
    license='MIT',
    packages=['sonos_lyrics', 'sonos_lyrics.lyrics', 'sonos_lyrics.players'],
    zip_safe=False,
    scripts=['bin/sonos-lyrics'],
    install_requires=[
        'requests',
        'html2text',
        'soco',
        'PyLyrics',
    ]
)
