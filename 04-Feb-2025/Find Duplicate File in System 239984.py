# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict= defaultdict(list)
        
        for path in paths:
            directory,*fileName=path.split()
            
            for f in fileName:
                start= f.find("(")+1
                end= f.find(")")
                key=f[start:end]
                file_type=f[:start-1]
                files= directory+"/"+file_type
                my_dict[key].append(files)
                
        res=[]
        for item,value in my_dict.items():
            if len(value)>1:
                res.append(value)
        return res

        

        

        
        