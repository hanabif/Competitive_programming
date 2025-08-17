# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        while i < len(chars):
            count = 1
            while (count + i) < len(chars) and chars[count + i] == chars[i]:
                count += 1 
            chars[index] = chars[i]
            index += 1
            if count > 1:
                string = str(count)
                chars[index:index + len(string)] = list(string)
                index += len(string)
            i += count
        return index


        