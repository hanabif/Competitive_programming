# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n,m= map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(input()))


direc=[(0,-1),(0,1),(-1,0),(1,0),(1,1),(-1,1), (-1,-1),(1,-1)]

def in_bound(i,j):
    if (0<=i<n) and (0<=j<m):
        return True
    return False
def checker(i,j):
    count=0
    for dx,dy in direc:
        nx=dx+i
        ny=dy+j

        if in_bound(nx,ny):
                        
            if arr[nx][ny]=="*":
                count+=1
    return count

is_valid=True
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j].isdigit():
            if checker(i,j)!=int(arr[i][j]):
                is_valid=False
        elif arr[i][j]==".":
            if checker(i,j)!=0:
                is_valid=False
if is_valid:
    print("YES")
else:
    print("NO")

            

        
