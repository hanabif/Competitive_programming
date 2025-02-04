# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        Hash=defaultdict(int)
        ans=[]
        for dom in cpdomains:
            value,domain=dom.split()
            value=int(value)
            subdomains=domain.split(".")
            for i in range(len(subdomains)):
                Hash[".".join(subdomains[i:])]+=value
        for val in Hash:
            ans.append(str(Hash[val])+" "+val)
       
        return ans
        
               
           