"""
this is a test

"""
#python Tab
import sys
import rlcompleter
import atexit
import os
try:
  import readline
except ImportError:
  import pyreadline as readline
  print "very fuck"
readline.parse_and_bind('tab: complete')
# windows
histfile = os.path.join(os.environ['HOMEPATH'], '.pythonhistory')
# linux
# histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter
