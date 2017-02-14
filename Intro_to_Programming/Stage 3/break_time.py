#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:55:42 2017

@author: timlatham
"""

import time
import webbrowser

total_breaks = 3
break_count = 0

print "This program started on " + time.ctime()
while break_count < total_breaks:
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")
    break_count += 1
