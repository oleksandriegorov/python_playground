import unittest


def recurse_search(words, start_idx, end_idx):
  if start_idx + 1 == end_idx:
    return end_idx
  elif words[start_idx] < words[end_idx]:
    return start_idx
  else:
    guess_idx = start_idx + ((end_idx - start_idx) // 2)
    if words[start_idx] > words[guess_idx]:
      return recurse_search(words, start_idx, guess_idx)
    else:
      return recurse_search(words, guess_idx, end_idx)


def find_rotation_point(words):
  if words == []:
    return -1
  else:
    return recurse_search(words, 0, len(words) - 1)


def find_rotation_point_iterative(words):
  if words == []:
    return -1
  else:
    # Find the rotation point in the list
    floor_index = 0
    ceiling_index = len(words) - 1
    if words[floor_index] < words[ceiling_index]:
      return 0
    else:
      while floor_index < ceiling_index:
        guess_index = floor_index + (ceiling_index - floor_index) // 2
        if words[guess_index] >= words[floor_index]:
          floor_index = guess_index
        else:
          ceiling_index = guess_index
        if floor_index + 1 == ceiling_index:
          return ceiling_index


# Tests

class Test(unittest.TestCase):

  def test_empty_list(self):
    actual = find_rotation_point([])
    expected = -1
    self.assertEqual(actual, expected)

  def test_nonrotated_list(self):
    actual = find_rotation_point(['apple', 'business', 'kettle'])
    expected = 0
    self.assertEqual(actual, expected)

  def test_small_list(self):
    actual = find_rotation_point(['cape', 'cake'])
    expected = 1
    self.assertEqual(actual, expected)

  def test_medium_list(self):
    actual = find_rotation_point(['grape', 'orange', 'plum',
                                  'radish', 'apple'])
    expected = 4
    self.assertEqual(actual, expected)

  def test_large_list(self):
    actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                  'undulate', 'xenoepist', 'asymptote',
                                  'babka', 'banoffee', 'engender',
                                  'karpatka', 'othellolagkage'])
    expected = 5
    self.assertEqual(actual, expected)

  # Are we missing any edge cases?


unittest.main(verbosity=2)