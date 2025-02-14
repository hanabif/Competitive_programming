# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import defaultdict

n=int(input())

for i in range(n):
    sum,res=0,0
    leng=int(input())
    s=input()
    left=set()
    right=defaultdict(int)

    for i in range(leng):
        right[s[i]]+=1
    length,maxim=0, len(right)
   
    for j in range(len(s)):
        left.add(s[j])
        right[s[j]]-=1
        if right[s[j]]==0:
            del right[s[j]] 
        length= len(left)+ len(right)
        maxim=max(length,maxim)
    print(maxim)

        
         
    


  