# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0
        for bill in bills:
            if bill == 5:
                count_5+=1
            elif bill == 10:
                count_10 +=1
                count_5-=1
                if count_5 < 0 :
                    return False
            else:
                if count_5 < 1:
                    return False
                if count_10 < 1 and count_5 < 3:
                    return False
                if count_10:
                    count_10-=1
                    count_5-=1
                else:
                    count_5-=3

        return True
                

        