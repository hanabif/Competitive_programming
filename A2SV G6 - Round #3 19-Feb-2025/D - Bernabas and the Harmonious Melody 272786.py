# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    counts = set(string)
    _min = float("inf")
    for c in counts:
        curr = 0
        l = 0
        r = len(string) - 1
        flag = False
        while l < r:
            if string[l] == string[r]:
                l += 1
                r -= 1
            else:
                if string[l] == c:
                    l += 1
                elif string[r] == c:
                    r -= 1
                else:
                    flag = True
                    break
                curr += 1

        if not flag:
            _min = min(curr, _min)
    print(_min if _min != float("inf") else -1)
    