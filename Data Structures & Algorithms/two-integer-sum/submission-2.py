class Solution:
    def twoSum(self, nums: nums[int], target: int) -> nums[int]:
        #using hashmaps in two sum?
        map_nums={}
        for i in range(0,len(nums)):
            if nums[i] not in map_nums : 
                map_nums[nums[i]]=[i]
            else : 
                map_nums[nums[i]].append(i)

        for i in range(0,len(nums)): 
            if (target-nums[i] in map_nums):
                have_index=map_nums[target-nums[i]]
                for j in have_index : 
                    if j != i:
                        return [i, j]