# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    k = int(data[idx + 1])
    q = int(data[idx + 2])
    idx += 3
    
    freq = [0] * (200002)  
    
    for _ in range(n):
        l = int(data[idx])
        r = int(data[idx + 1])
        freq[l] += 1
        if r + 1 <= 200000:
            freq[r + 1] -= 1
        idx += 2
    
    
    for t in range(1, 200001):
        freq[t] += freq[t - 1]
    
    
    prefix = [0] * (200002)
    for t in range(1, 200001):
        prefix[t] = prefix[t - 1] + (1 if freq[t] >= k else 0)
    
    
    for _ in range(q):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        print(prefix[b] - prefix[a - 1])

if __name__ == "__main__":
    main()