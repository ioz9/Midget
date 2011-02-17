import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pyramid',
    'sqlalchemy',
    'WebError',
    "nose"]

setup(name='Midget',
      version='0.10',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="nose.collector",
      entry_points="""\
      [paste.app_factory]
      main = midget:main
      """,
      paster_plugins=['pyramid'],
)

