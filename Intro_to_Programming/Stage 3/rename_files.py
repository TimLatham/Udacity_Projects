#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:25:24 2017

@author: timlatham
"""
import os
import string

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir("/Users/timlatham/Desktop/prank")
    print file_list
    saved_path = os.getcwd()
    os.chdir("/Users/timlatham/Desktop/prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        print "Old Name - " + file_name
        print "New Name -" + file_name.translate(None,'0123456789')
        os.rename(file_name, file_name.translate(None,'0123456789'))
    os.chdir(saved_path)
    
rename_files()