# LeetCode3
문제 링크 : 

**문제 내용**  


**제한조건**  

**입출력 예**  
input

output


**내가 푼 코드**  
```python

```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
def lengthOfLongestSubstring(s):
    subStr = ''
    maxLength = 0
    for i in range(len(s)):
      if s[i] in list(subStr):
        subStr = subStr[subStr.index(s[i])+1:]
      subStr+=s[i]
      maxLength = max(maxLength,len(subStr))#1
        
    return maxLength
```
시간복잡도 O(N)
