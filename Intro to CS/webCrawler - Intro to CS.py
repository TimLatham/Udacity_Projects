# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:52:38 2017

@author: tim.latham
"""

start_link = page.find('<a href=')

start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)

url = page[start_quote + 1 : end_quote]