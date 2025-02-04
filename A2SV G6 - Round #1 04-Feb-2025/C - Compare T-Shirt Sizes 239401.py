# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

n= int(input())
for i in range(n):
    a,b=input().split()
    a,b=list(a),list(b)

    if len(a)==len(b)==1:
        if a==b:
            print("=")
        elif ("M" in a and "L" in b) or ("S" in a and "M" in b) or ("S" in a and "L" in b):
            print("<")
        else:
            print(">")
    else:
        ax,bx=0,0
        for i in a:
            if i=="X":
                ax+=1
            
        for j in b:
            if j=="X":
                bx+=1
        
        if "S" in a and "S" in b:
            if ax>bx:
                print("<")
            elif ax<bx:
                print(">")
            else:
                print("=")
        elif "L" in a and "L" in b:
            if ax>bx:
                print(">")
            elif ax<bx:
                print("<")
            else:
                print("=")
        elif ("S" in a and "L" in b) or ("S" in a and "M" in b) or ("M" in a and "L" in b):
            print("<")
        elif ("L" in a and "S" in b) or ("L" in a and "M" in b) or ("M" in a and "S" in b):
            print(">")
        
        else:
            print("=")


