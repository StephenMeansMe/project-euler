# ======================================================================
# PROJECT EULER PROBLEM NO. 18: LARGEST PATH SUM
# ----------------------------------------------------------------------
# Given a triangular array of numbers, find the largest path sum.
# ======================================================================

# import numpy as np

# Spanning tree, biiiiiiiiitch!
#class node(object):
#    def __init__(self, value, children = []):
#        self.value = value
#        self.children = children

triangle = [] # initialize triangle

with open('euler18.txt','r') as f:
    for line in f:
        if len(line):
            new_row = line.split(' ')
            new_row = [int(x) for x in new_row]
        triangle.append(new_row)

print("Triangle has "+str(len(triangle))+" rows.")
print(triangle[0])

for i in range(len(triangle)-1, 0, -1):
    #print(i, len(triangle[i-1]))
    for j in range(len(triangle[i-1])):
        #print(j, triangle[i-1][j], triangle[i][j], triangle[i][j+1])
        triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])

print(triangle[0])
