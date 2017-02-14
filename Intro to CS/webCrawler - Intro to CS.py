# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:52:38 2017

@author: tim.latham
"""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
    
print_all_links('this <a href="test1">link 1</a> is <a href="test2">link 2</a> a <a href="test3">link 3</a>')