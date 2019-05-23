#!/usr/bin/env python

import time
from contextlib import contextmanager

@contextmanager
def spenttime():
  try:
    starttime = time.time()
    yield starttime
  finally:
    print(time.time()-starttime)

if __name__ == '__main__':
  with spenttime():
    time.sleep(2)
    with spenttime():
      time.sleep(1)
    time.sleep(1)