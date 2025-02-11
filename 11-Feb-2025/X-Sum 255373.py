# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

n=int(input())
for _ in range(n):
    n,m= map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(list(input().split()))

    diagonal=[(-1,1),(1,1),(1,-1),(-1,-1)]

    def in_bound(i,j):
        if (0<=i<n) and (0<=j<m):
            return True
        return False
    
    def diagonals(i,j):
        sum=0
        for x,y in diagonal:
            ni=x+i
            nj=y+j
            while in_bound(ni,nj):
                sum+=int(arr[ni][nj])
                ni=ni+x
                nj=nj+y
        return sum


    maxSum,total=0,0
    for i in range(n):
        for j in range(m):
            total=diagonals(i,j)+int(arr[i][j])
            maxSum=max(maxSum,total)
    print(maxSum)


    

            
