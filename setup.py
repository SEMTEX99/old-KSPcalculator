import os
import re
import sys

import setuptools

SRC = os.path.abspath(os.path.dirname(__file__))


def get_version():
    with open(os.path.join(SRC, 'kspalculator/__init__.py')) as f:
        for line in f:
            m = re.match("__version__ = '(.*)'", line)
            if m:
                return m.group(1)
    raise SystemExit("Could not find version string.")


if sys.version_info.major == 2:
    if sys.version_info < (2, 7):
        sys.exit('Python version not supported.')
    entry_points = None
    install_requires = ['enum34>=1.0']
    print("Note that you need Python3 to execute kspalculator script.")
elif sys.version_info.major == 3:
    if sys.version_info < (3, 4):
        sys.exit('Python version not supported.')
    entry_points = {'console_scripts': ['kspalculator=kspalculator.__main__:main']}
    install_requires = None
else:
    sys.exit('Python version not supported.')

setuptools.setup(
    #TODO finish this script
)
