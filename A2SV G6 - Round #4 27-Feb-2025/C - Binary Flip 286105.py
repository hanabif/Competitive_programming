# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

def can_transform(t, test_cases):
    results = []
    for n, a, b in test_cases:
        zero_count = 0
        one_count = 0
        flip_possible = [False] * n

       
        for i in range(n):
            if a[i] == '0':
                zero_count += 1
            else:
                one_count += 1
            if zero_count == one_count:
                flip_possible[i] = True

        
        flip = False
        for i in range(n - 1, -1, -1):
            if flip:
                a_i = '1' if a[i] == '0' else '0'  
            else:
                a_i = a[i]

            if a_i != b[i]:
                if flip_possible[i]:  
                    flip = not flip  
                else:
                    results.append("NO")
                    break
        else:
            results.append("YES")

    return results


import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    a = data[index + 1]
    b = data[index + 2]
    test_cases.append((n, a, b))
    index += 3


print("\n".join(can_transform(t, test_cases)))
