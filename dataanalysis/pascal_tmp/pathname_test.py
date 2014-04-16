# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:50:23 2013

@author: pascal
"""

import os

print "cwd:", os.getcwd()
print "basename:", os.path.basename(__file__)
print "abspath:", os.path.abspath(__file__)
print "dirname:", os.path.dirname(__file__)

#os.path.abspath = os.path.dirname + os.path.basename
# vs
#os.path.dirname(filename) + os.path.basename(filename) == filename

#To get the dirname of the absolute path
print "dirname of abs path:", os.path.dirname(os.path.abspath(__file__))


parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print parent_dir
