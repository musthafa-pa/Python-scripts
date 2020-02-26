#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:19:53 2020

@author: mustafa
"""

import time
import subprocess

def webSpeed():
    website = raw_input("Enter name of the website:  ")
    print(website)
    cmd = 'wget https://%s' % (website)
    print(cmd)
    temp = subprocess.call(cmd, shell="TRUE")
    print(temp)
    

webSpeed()