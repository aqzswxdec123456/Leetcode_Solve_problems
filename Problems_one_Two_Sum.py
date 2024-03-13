"""
參考 https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

簡單敘述 
nums = list 內有整數
target = list 相加以後得到的值(整數)

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

思路探討 1. 

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      length = len(nums) # 計算 nums 列表內有幾筆
      for i in range(length): # 將 nums 一筆一筆拿出來當作i 
        for j in range(i + 1,length): # 將 nums 一筆一筆拿出來當作j ，i的下一筆當開始點，結束則是length
          if nums[i] + nums[j] == target: # 判斷 當這這一筆 與 下一筆 相加 = 變數 target
            return [i, j] # 回應 這兩筆 num 的 index 位置 
      return []


# 內建函數 enumerate
class Solution:
    def twoSum(self, nums, target):
        num_to_index = {} # 宣告一個字典
        for index, num in enumerate(nums): # 把索引、值 透過 內建函數拿出來排列
            other = target - num   # 宣告一個 變數 用減的
            if other in num_to_index: # 判斷 後面的值是要找到的，如果是就 return 
                return [num_to_index[other], index] 
            num_to_index[num] = index # 把 list 值 變成字典 key
        return []
