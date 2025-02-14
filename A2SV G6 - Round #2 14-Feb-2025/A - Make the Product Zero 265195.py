# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

n=int(input())
array = list(map(int, input().split()))
res=0
if 0 in array:
    res=0
else:
    for i in range(len(array)):
        array[i]=abs(array[i])
    res=min(array)
print(res)

