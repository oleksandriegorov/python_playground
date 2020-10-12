#!/usr/bin/env python3

# Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

## ? capital letters and numbers only?
## ? are symbols unique?
## ? are they already sorted?
## ? use additional space allowed? if not - linked list is likely the case


# points
## there is no point to compress if there are only 2 symbols
## O(n) space
## O(n) time
## special cases

def compress_string(s: str):
  count = 0
  last_letter = ''
  compress_s = ''
  if not s or s == '':
    return s
  for idx in range(0,len(s)):
    if idx == 0:
      last_letter = s[idx]
      count = 1
    elif s[idx] == last_letter:
      count += 1
      if idx == len(s)-1:
        if count >= 2:
          compress_s+=last_letter+str(count)
        else:
          compress_s+=last_letter*count
    # if new character is not the same as previous one
    else:
      if count >= 2:
        compress_s += last_letter + str(count)
      else:
        compress_s += last_letter * count
      last_letter = s[idx]
      count = 1

  return compress_s if len(compress_s) < len(s) else s

import unittest
class Test(unittest.TestCase):
  def testempty(self):
    expected = ''
    actual = compress_string('')
    self.assertEqual(expected,actual)

  def testnone(self):
    expected = None
    actual = compress_string(None)
    self.assertEqual(expected,actual)

  def testnocompression(self):
    expected = "AABBCC"
    actual = compress_string("AABBCC")
    self.assertEqual(expected,actual)

  def testcompression(self):
    expected = "A3BC2D4"
    actual = compress_string("AAABCCDDDD")
    self.assertEqual(expected,actual)

unittest.main(verbosity=2)