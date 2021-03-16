def solution(n):
    number=''
    answer=0
    while n > 0:
        div = n // 3
        mod = n % 3
        n = div
        number += str(mod)
    # 45 = 1200(3) = number[::-1]
    # 0021(3) = ?(10)
    for idx, num in enumerate(number[::-1]):
        answer += int(num)*(3**idx)
    return answer

n=45
s = solution(n)
print(s)