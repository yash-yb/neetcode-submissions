class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums: 
            if i in dict.keys() : 
                dict[i]+=1
            else : 
                dict[i]=1
        
        for i in dict.keys():
            if dict[i]>1:
                return True
        
        else : 
            return False
        