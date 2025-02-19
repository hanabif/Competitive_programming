# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter

def can_transform(s, t, p):
    
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    if i < len(s):  # If not all of s was found in t
        return "NO"
    
    
    s_p_count = Counter(s) + Counter(p)  
    t_count = Counter(t)  # Required characters
    
    for char in t_count:
        if t_count[char] > s_p_count[char]:  
            return "NO"
    
    return "YES"


q = int(input().strip())

results = []
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    
    results.append(can_transform(s, t, p))


print("\n".join(results))
