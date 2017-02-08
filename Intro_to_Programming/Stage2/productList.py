# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 11:42:46 2017

@author: tim.latham
"""

# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    product = 1
    count = 0
    if len(list_of_numbers) == 0:
        return product
    else:    
        while count < len(list_of_numbers):
            product = product * list_of_numbers[count]
            count += 1
    return product

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1