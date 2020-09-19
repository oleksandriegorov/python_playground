#!/usr/bin/env python

import unittest

def nfib(number:int):
  if number in [0,1]:
    return number
  else:
    parent=1
    grandparent=0
    for _ in range(1,number):
      current = parent + grandparent
      grandparent = parent
      parent = current
    return current

class Test(unittest.TestCase):
  def test_zeroth_fib(self):
    res = nfib(0)
    expected = 0
    self.assertEqual(res,expected)

  def test_1st_fib(self):
    res = nfib(1)
    expected = 1
    self.assertEqual(res,expected)

  def test_2md_fib(self):
    res = nfib(2)
    expected = 1
    self.assertEqual(res,expected)

  def test_5th_fib(self):
    res = nfib(5)
    expected = 5
    self.assertEqual(res,expected)

  def test_7th_fib(self):
    res = nfib(7)
    expected = 13
    self.assertEqual(res, expected)

  def test_10th_fib(self):
    res = nfib(10)
    expected = 55
    self.assertEqual(res,expected)

unittest.main(verbosity=2)
