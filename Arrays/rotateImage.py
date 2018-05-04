'''
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
     
'''


import numpy

def rotateImage(a):
    #mat = numpy.flipud(a)
    #mat1 = numpy.transpose(mat)
    #return mat1
    
    m=zip(*reversed(a))
    return list(m)
