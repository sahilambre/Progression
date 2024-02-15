def isAnagram(s, t):
    # If lengths of the strings are not equal, they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Count occurrences of each character in both strings
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    # Compare character counts of both strings
    for char in countS:
        if countS[char] != countT.get(char, 0):
            return False
    
    return True

# Example usage:
# s = "anagram"
# t = "nagaram"
# print(isAnagram(s, t))  # Output: True

s = "rat"
t = "car"
print(isAnagram(s, t))  # Output: False
