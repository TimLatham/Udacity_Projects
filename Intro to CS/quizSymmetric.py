# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(p):
    if len(p) == 0:
        return True
    if len(p) != len(p[0]): # row and column counts don't match, not symmetric
        return False
    column_counter = 0
    while column_counter < len(p):
        row_counter = 0
        column_list = []
        row_list = p[column_counter]
        while row_counter < len(p):
            column_list.append(p[row_counter][column_counter])
            row_counter += 1
        #print row_list, column_list
        if column_list != row_list:
            return False
        column_counter += 1
    return True
        
    
print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False