
from setuptools import setup
import amathon
from amathon import __version__, __license__, __author__


# nothisng test

# build desitribution package
setup(
    name             = 'amathon',
    version          = __version__,
    description      = 'Amazon api wrapper for Python 3.x',
    long_description = amathon.__doc__,
    author           = __author__,
    url              = 'https://github.com/y42sora/Amathon',
    keywords         = 'amazon, python3',
    license          = __license__,
    packages         = ('amathon',),
    classifiers      = ["Development Status :: 3 - Alpha",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Libraries :: Python Modules"]
    )

