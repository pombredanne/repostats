#!/usr/bin/python
import os
import sys
import copy
import subprocess

print os.path.abspath(os.getcwd() + '/.helpers/')
sys.path.insert(0, os.path.abspath(os.getcwd() + '/.helpers'))


import load as load


keywords = ['load=','ls','file=', 'save', 'lang', 'clear']
import getopt
opts, remainder = getopt.getopt(sys.argv[1:],'p:l',keywords)
for o,p in opts:
    if o in ('-n','--load'):
        load.loadRepo(p);
    elif o in ('-l','--ls'):
        x = 0
        #list files
    elif o in ('-f', '--file'):
        x = 0
        #do file analytics
    elif o in ('-s', '--save'):
        x = 0
        #save repository
    elif o is '--lang':
        x = 0
        #print langs
    elif o is '--clear':
        x = 0
        #clear
        
