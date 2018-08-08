import unittest
from unittest import TestCase

from .github_check import *

from github_check import check_github_repo
print('HELLO')
def get_suite():
  """Return a unittest.TestSuite."""
  check_github_repo()
  print('WORLD')
  import github_check.tests
  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(github_check.tests)
  return suite