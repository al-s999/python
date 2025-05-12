from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        count_s = Counter(s)
        count_t = Counter(t)
        
        result = []
        
        for char in count_t:
            if count_t[char] > count_s[char]:
                result.extend([char] * (count_t[char] - count_s[char]))
        
        return ''.join(result)

# Contoh penggunaan
solution = Solution()
s = "abcd"
t = "abcde"
print(solution.findTheDifference(s, t))  # Output: 'e'

s = "aabbcc"
t = "aabbccc"
print(solution.findTheDifference(s, t))  # Output: 'c'