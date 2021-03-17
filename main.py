#키패드 누르기 소수 만들기
from itertools import combinations

def solution(nums):
    answer = len(list(combinations(nums, 3)))
    for l in list(combinations(nums, 3)):
      for i in range(2,sum(l)):
        if sum(l) % i == 0:
          answer -=1
          break
      
    return answer



nums = [1,2,3,4]
s = solution(nums)
print(s)
