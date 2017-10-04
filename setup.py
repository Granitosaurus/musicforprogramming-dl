from setuptools import setup

setup(
    name='musicforprogramming',
    version='1',
    url='https://github.com/Granitosaurus/musicforprogramming-dl',
    py_modules=['musicforprogramming'],
    entry_points={'console_scripts': ['musicforprogramming = musicforprogramming:cli']},
    install_requires=['click', 'requests'],
    license='GPLv3',
    author='granitosaurus',
    author_email='bernardas.alisauskas@protonmail.com',
    description='Music downloader for musicforprogramming.net'
)
