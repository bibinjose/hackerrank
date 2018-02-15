class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i

numbers=[1,2,3,4,5,6]
target=5
sol=Solution()
print(sol.twoSum(numbers,target))