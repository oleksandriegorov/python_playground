#!/usr/bin/env python3

# Given an array of integers greater than zero, find if there is a way to split the array (without reordering any element) such that the numbers before the split add up to the numbers after the split. If so print the two resulting arrays
# I:[5,2,3]
# o:[5],[2,3]

# i:[2,3,2,1,1,1,2,1,1]
# o:[2,3,2],[1,1,1,2,1,1]

# Basic idea is to find sum right to left and then left to right. Whenever a sum for an element_index in left to right is
# equal to element_index+1 element is a division point

import unittest

# Possible improvements:
# - when going backwards I could just stop at a matching sum with a forward sum
# current complexity is 0(3*n)

def divide_array_equal_sum(int_list: list):
  l_list = len(int_list)
  sum_before = [0] * l_list
  sum_after = [0] * l_list
  tmp_sum = 0
  for idx in range(0,l_list):
    tmp_sum += int_list[idx]
    sum_before[idx] += tmp_sum
  tmp_sum = 0
  for idx in range(l_list-1,-1,-1):
    tmp_sum += int_list[idx]
    sum_after[idx] += tmp_sum
  for idx in range(0,l_list-1):
    if sum_before[idx] == sum_after[idx+1]:
      return [int_list[0:idx+1], int_list[idx+1::]]

  pass
  return False

class Test(unittest.TestCase):

    def test_firstinthree(self):
        actual = divide_array_equal_sum([5,2,3])
        expected = [[5],[2,3]]
        self.assertEqual(actual,expected)

    def test_thirdinnine(self):
        actual = divide_array_equal_sum([2,3,2,1,1,1,2,1,1])
        expected = [[2,3,2],[1,1,1,2,1,1]]
        self.assertEqual(actual,expected)

    def test_noway_three(self):
        actual = divide_array_equal_sum([1,1,3])
        expected = False
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)