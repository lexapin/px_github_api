import os
from setuptools import setup, find_packages

__version__ = '0.0.1'

build = os.environ.get('BUILD_NUMBER', 0)
if build:
  __version__ += '-%s' % build

setup(
  name='github-check',
  version=__version__,
  packages=find_packages(),
  include_package_data=True,
  zip_safe=False,
  platforms='any',
  scripts=[
    'github_check/bin/github-check',
  ],
  test_suite='github_check.tests.get_suite',
)