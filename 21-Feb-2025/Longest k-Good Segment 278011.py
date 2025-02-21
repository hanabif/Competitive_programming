# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
number_input,t=map(int,input().split())
 
arr=list(map(int,input().split()))
 
num=defaultdict(int)
 
left,ol,orr=0,0,0
 
ans=0
 
for r in range(number_input):
    num[arr[r]]+=1
    while len(num) > t:
        num[arr[left]]-=1
        if num[arr[left]]==0:
            del num[arr[left]]
        left+=1
    if ans < r-left+1:
        ans=r-left+1
        ol=left
        orr=r
print(ol+1,orr+1)