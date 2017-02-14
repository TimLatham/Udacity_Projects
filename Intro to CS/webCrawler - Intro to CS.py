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

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            link.append(url)
            page = page[endpos:]
        else:
            break
    
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            
            
            union (tocrawl, get_all_links(content)
            crawled.append(page)
    return crawled

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
    
'''
def add_to_index(index, keyword, url):
    for entry in index: 
        if entry[0] == keyword: 
            entry[1].append(url) 
            return 
            

    
    
index = []
add_to_index(index, 'udacity', 'http://udacity.com')
index.append([keyword, [url]])
print index
'''


links = get_all_links('http://www.udacity.com/cs101x/index.html')
print links