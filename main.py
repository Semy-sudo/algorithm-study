def lengthOfLongestSubstring(s):
    subStr = ''
    maxLength = 0
    for i in range(len(s)):
      if s[i] in list(subStr):
        subStr = subStr[subStr.index(s[i])+1:]
      subStr+=s[i]
      maxLength = max(maxLength,len(subStr))#1
        
    return maxLength

s = "dvdf"
l = lengthOfLongestSubstring(s)
print(l)