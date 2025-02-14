# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t=int(input())
arr=[]
for _ in range(t):
    
    n=int(input())
    arr = []
    for i in range(n):
        arr.append(list(input()))
    
    
    ans=0
    for i in range(n):
        for j in range(n):
            zeros, ones=0,0
            temp=[arr[i][j],arr[n-j-1][i],arr[n-i-1][n-j-1],arr[j][n-1-i]]
            for t in temp:
                if t=="0":
                    zeros+=1
                else:
                    ones+=1
            
            ans+=min(zeros,ones)
    
    print(ans//4)
            

            

    
    