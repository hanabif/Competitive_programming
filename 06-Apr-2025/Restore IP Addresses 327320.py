# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res= []

        def back(i , dots , store):
            if dots == 4 and i == len(s):
                res.append(store[:-1])
                return 
            if dots > 4:
                return
            
            for j in range(i , min( i + 3 , len(s))):
                if int(s[i:j + 1]) < 256 and ( i == j or s[i]!= '0'):
                    back( j + 1, dots + 1 , store + s[i:j + 1] + ".")
        back(0,0,"")
        return res
        