# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:52:47 2020

@author: Aron Arceo
Leetcode reverse in python! can support both absolute and otherwise
"""

class Solution:
  def reverse(self, x: int)->int:
    rnum = int(str(abs(x))[::-1])
    if(x==0 or rnum < -2**31 or rnum > 2**31-1):
      return(0)
    if(x>0):
      return(rnum)
    else:
      return(rnum*-1)

tc = Solution()
print(tc.reverse(-123))