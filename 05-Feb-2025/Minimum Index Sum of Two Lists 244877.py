# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        Hash={}
        for i in range(len(list1)):
            Hash[list1[i]]=i
        mini=float(inf)
        for j in range(len(list2)):
            if list2[j] in Hash:
                summ= Hash[list2[j]]+j
               
                if summ<mini:
                    mini=summ
                    res=[]
                    res.append(list2[j])
                elif summ==mini:
                    res.append(list2[j])
        return res
               

        