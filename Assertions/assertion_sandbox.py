#!/usr/bin/env python

def newhash(text):
  import random
  '''
  :param text: string
  :return: char from a: int 97 to z: int 122
  '''
  return chr(random.randint(97,122))

def mailhome(emailaddress,hashtype='legacy'):
  '''
  :param emailaddress: string, email address or email user
  :param hashtype: string, 'legacy' or 'new' values are accepted. defaults to 'legacy'
  :return: string of a path to email user mailhome
  '''
  import re
  # Replace all '@' chars to '.'
  emailuser=emailaddress.replace('@','.').lower()
  # Compile regex to ensure proper mailhome generated
  pathpattern=re.compile("^\/(h|mailboxes)\/[a-z]\/[a-z]\/%s"%emailuser)
  if hashtype == 'new':
    path='/h/'+newhash(emailuser.split('.')[0])+'/'+newhash(emailuser.split('.')[1])+'/'+emailuser
  else:
    path='/mailboxes/'+emailuser.split('.')[0][0]+'/'+emailuser.split('.')[1][0]+'/'+emailuser
  assert re.match(pathpattern,path)
  return path


if __name__ == '__main__':
  import random
  import re
  print(mailhome('test@test.com',hashtype='new'))
