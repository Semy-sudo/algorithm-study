#예상 대진표
#다른사람 풀이
## 비트 XOR
def solution(n,a,b):
    print((a-1)^(b-1))
    return ((a-1)^(b-1)).bit_length() 
n = 8
a = 4 #11
b = 7 #
s = solution(n,a,b)
print(s)