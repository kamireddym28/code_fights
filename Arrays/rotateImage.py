import numpy

def rotateImage(a):
    #mat = numpy.flipud(a)
    #mat1 = numpy.transpose(mat)
    #return mat1
    
    m=zip(*reversed(a))
    return list(m)
