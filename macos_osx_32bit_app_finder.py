#!/usr/bin/env python
# 2017-08-24 macos_osx_32bit_app_finder.py
# Florian Paul Hoberg
# This will find your 32bit apps
# on your local MacOS / OSX system
# usage: macos_osx_32bit_app_finder.py

import sys
import os
from subprocess import check_output

before=6
after=0
v_systemprofile = check_output(["system_profiler", "SPApplicationsDataType"])
f_systemprofile = "/tmp/systemprofile.tmp.txt"

def write_systemprofile():
    """ Write systemprofile file """
    with open(f_systemprofile, 'wb') as f_spfw:
     f_spfw.write(v_systemprofile)


def append(size, data, x):
    """ Append/pop buffer """
    if len(data)>=size:
        data.pop(0)
    data.append(x)


def readconv_systemprofile():
    """ Read/convert systemprofile file """
    buffer = []
    with open(f_systemprofile, 'r') as f_spfwr:
        print "Installed 32bit Apps on your system:"
        print "-"*40
        for line in f_spfwr:
            line=line.strip()
            if "(Intel): No" in line:
                if buffer:
                    print(buffer)
                buffer=[]
                after_count=after
                while after_count<after:
                    after_count+=1
                    try:
                        line=f.next().strip()
                    except: pass
                    else:
                        print line
                        if "match" in line:
                            after_count=0
            else:
                append(before,buffer,line)
 

write_systemprofile()
readconv_systemprofile()
