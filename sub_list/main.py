# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 04:55:51 2019

@author: yumi3
"""

def check_sublist(A,B):
    #create a dict of B
    dict = {i : i for i in B }
    #check if elements in A is in B too
    for i in A:
        if i  not in dict:
            return False
    return True

'''
Test 1 -True
'''
A = [-2, 1, 3]
B = [-99, -100, -2, 0, 1, 2, 3, 98, 100]
print(check_sublist(A,B))

'''
Test 2 -False
'''
A = [-2, 1, 3, 4, 6]
B = [-99, -100, -2, 0, 4, 5, 36, 98, 100]
print(check_sublist(A,B))

'''
Test 3 -True
'''
A = [-2, 1, 3, 100, -99]
B = [-99, -100, -2, 0, 1, 2, 3, 98, 100]
print(check_sublist(A,B))


'''
Test 4 -False
'''
A = [-2, 1, 3, 0, 54]
B = [-99, -100, -2, 0, 1, 2, 3, 98, 100]
print(check_sublist(A,B))