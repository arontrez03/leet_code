# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:51:26 2020

@author: Aron Arceo
Leetcode roman to int!
"""

class Solution:
    def romanToInt(self, s: str) -> int:
      thisdict = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
      sum = 0
      previous = 0
      if(len(s) == 1):
        sum = thisdict[s]
      else:
        for element in s:
          current = thisdict[element]
          sum += thisdict[element]
          if(previous < current):
            sum -= (previous*2)
          previous = current
      return(sum)
test = Solution()
print(test.romanToInt("IL"))