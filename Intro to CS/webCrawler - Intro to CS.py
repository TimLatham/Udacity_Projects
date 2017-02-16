# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:52:38 2017

@author: tim.latham
"""
import time

def time_execution(code):
    start = time.clock() # start the clock
    result = eval(code) # evaluate any string as if it is a Python command
    run_time = time.clock() - start # find the difference in start and end time
    return result, run_time # return the result of the code and the time taken

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
            links.append(url)
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
            
            
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return crawled

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
    
def make_big_index(size):
    index = []
    letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index
        
def make_string(p):
    s = ""
    for e in p: # for each element in the list p
        s = s + e # add it to string s
    return s

def add_to_index(index, keyword, url):
    for entry in index: 
        if entry[0] == keyword: 
            entry[1].append(url) 
            return 
    
index = []
add_to_index(index, word, 'fake')
#index.append([keyword, [url]])
print index



links = get_all_links('http://www.udacity.com/cs101x/index.html')
print links