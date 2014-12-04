#!/usr/bin/python

import fnmatch
import os

path = '/home/dhaval/Downloads'
pattern = '*.py'

for root,dirs,files in os.walk(path):
   for filename in fnmatch.filter(files,pattern):
       print(os.path.join(root,filename))
