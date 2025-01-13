from typing import List

word1 = "ab"
word2 = "pqrs"
s = "abc"
t = "acbgdc"
nums = [0,1,0,3,12]

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      # O(n) 2 pointers
      # we're checking if 's' is a substring of 't'
      # start by setting pointers 'i' and 'j' at 0 for the 2 strings
      # while both pointers are lesser than the len of the 2 strings
      # we only want to move pointer 's' if there's a match with 'j'
      # we increment 'j' in both cases, so we do that outside of if statement
      # then we return true if pointer 'i' is equal to length of 's'
      # because that means we've gotten to the end of the string
      # and there's a full match of the substring
      i, j = 0, 0
      while i < len(s) and j < len(t):
        if s[i] == t[j]:
          i += 1
        j += 1
      return True if i == len(s) else False

    def moveZeroes(self, nums: List[int]) -> None:
      # O(n) using 2 pointers
      # instead of moving 0s to the right
      # focus on moving non 0s to the left
      # left and right will start at the beginning of the list
      # iterate through the list, whenever right pointer is a non 0
      # swap the value with the one on left pointer
      # then immediately increment left pointer
      left = 0
      for right in range(len(nums)):
        if nums[right]:
          nums[left], nums[right] = nums[right], nums[left]
          left += 1
      return nums
      
    def mergeAlternately(self, word1: str, word2: str) -> str:
      # O(n)
      # setup 2 variables to hold the length of the 2 strings
      # setup 2 pointers to use as indexes for the 2 strings
      # while the index of either string is smaller than length of either string
      # if index of first string is < than length of first string
      # then add the indexed char to res
      # then increment the index
      # perform same steps for the second string
      # return result
      l1 = len(word1)
      l2 = len(word2)
      p1 = 0
      p2 = 0
      res = []

      while p1 < l1 or p2 < l2:
        if p1 < l1:
          res += word1[p1]
          p1 += 1
        if p2 < l2:
          res += word2[p2]
          p2 += 1
          
      return ''.join(res)    

solution = Solution()
result = solution.isSubsequence(s, t)
# result = solution.moveZeroes(nums)
# result = solution.mergeAlternately(word1, word2)
print(result)