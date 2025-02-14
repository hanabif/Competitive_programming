# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

sum=0
for i in range(n):
    for j in range(n):
        if i==j:
            sum+=arr[i][j]
        if i+j==n-1:
            sum+=arr[i][j]
        if i==(n-1)//2 :
            sum+=arr[i][j]
        if j==(n-1)//2:
            sum+=arr[i][j]
sum-= 3*arr[(n-1)//2][(n-1)//2]


            
print(sum)
