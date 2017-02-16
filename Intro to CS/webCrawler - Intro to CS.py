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
    return links
    
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    graph = {} # <url>, [list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url) # this will look up in the dictionary the entry that corresponds to the index, which is going to be thelist or urls
    else:
        # not found, add new keyword to index
        index[keyword] = [url]
    """for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])"""

def lookup(index, keyword):
    if keyword in index: # instead of a loop, check to see if keyword is in the index
        return index[keyword] # if it is, use dictionary lookup
    else:
        return None # if the keyword is not in the index
    """for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None"""

def make_string(p):
    s = ""
    for e in p: # for each element in the list p
        s = s + e # add it to string s
    return s
        
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

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
        
            for node in graph:
                if page in graph[node]:
                    newrank += ranks[node] * d / len(graph[node])
            newranks[page] = newrank
        ranks = newranks
    return ranks
    
# add_to_index(index, word, 'fake')
# print index



links = get_all_links('http://www.udacity.com/cs101x/index.html')
print links