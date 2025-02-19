# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

def decrypt_repeating_cipher(n, t):
    result = []
    position = 0
    step = 1

    while position < n:
        result.append(t[position])
        position += step
        step += 1  

    return ''.join(result)


n = int(input().strip())
t = input().strip()


print(decrypt_repeating_cipher(n, t))
