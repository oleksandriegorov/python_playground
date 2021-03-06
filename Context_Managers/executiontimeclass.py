#!/usr/bin/env python

import time

class measuretime():
  def __init__(self):
    self.starttime = 0

  def __enter__(self):
    self.starttime = time.time()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    print(time.time() - self.starttime)

if __name__ == '__main__':
  with measuretime():
    with measuretime():
      time.sleep(2)
      with measuretime():
        time.sleep(1)
    time.sleep(3)
