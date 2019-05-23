#!/usr/bin/env python

from contextlib import contextmanager

@contextmanager
def managed_file(name):
  try:
    f = open(name,'w')
    yield f
  finally:
    f.close()

if __name__ == '__main__':
  with managed_file('dummyfilefunc') as f:
    f.write('Hello World 123 abc xyz')
