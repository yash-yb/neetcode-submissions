class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1={}
        map2={}
        for i in s:
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
        
        for i in t:
            if i in map2:
                map2[i]+=1
            else:
                map2[i]=1
        
        if map1.keys()==map2.keys():
            for j in map1.keys():
                if j not in map2:
                    return False
                if map1[j]!=map2[j]:
                    return False
            else : 
                return True
        else : 
            return False