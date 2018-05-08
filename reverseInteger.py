class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x>0:
            n = 1
        else:
            n = -1
        x = x*n
        z= int((str(x)[0:])[::-1])
        return z*n*(z<0x7FFFFFFF)
