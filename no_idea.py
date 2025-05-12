from collections import Counter

# Skip a line
input()

# Just count all the numbers
nums = Counter(input().split())

# Sum up counts of numbers we like
current_mood = sum(nums[n] for n in input().split())

# Subtract the numbers we dislike
current_mood -= sum(nums[n] for n in input().split())

print(current_mood)