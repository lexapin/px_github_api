import unittest

from github_check import check_github_repo

class TestMain(unittest.TestCase):
  """docstring for TestMain"""
  
  def test_main(self):
    self.assertIsNone(check_github_repo())

print('test loaded')