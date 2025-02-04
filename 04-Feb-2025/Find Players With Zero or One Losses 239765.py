# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser=defaultdict(int)
        winner=defaultdict(int)
        l,w=[],[]
        for win, lose in matches:
            winner[win]+=1
            loser[lose]+=1
        
        for i in winner:
            if loser[i] == 0:
                w.append(i)
        for i in loser:
            if loser[i] == 1:
                l.append(i)
        return [sorted(w),sorted(l)]

            
                