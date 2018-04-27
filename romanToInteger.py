'''
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

-->Input: "LVIII"
   Output: 58
   Explanation: C = 100, L = 50, XXX = 30 and III = 3.
--->Input: "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        r = d[s[-1]]
        
        for i in range(len(s)-2,-1,-1):
            if d[s[i]]<d[s[i+1]]:
                r -= d[s[i]]
            else:
                r += d[s[i]]
        return r
