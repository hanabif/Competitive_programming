# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

n=int(input())
for i in range(n):
    s="$"+input()
    if (len(s)-1)%2!=0:
        print("NO")
    else:
        split=len(s)//2
        s1=s[1:split+1]
        s2=s[split+1:]
        if s1==s2:
            print("YES")
        else:
            print("NO")