def solution(p,l):
  ans = 0
  m = max(p)
  while True:
    v = p.pop(0)
    if m==v:
      ans +=1
      if l==0:
        break
      else:
        l-=1
      m = max(p)#다시 정하기
    else:
      p.append(v)
      if l==0:
        l = len(p)-1
      else:
        l-=1

  return ans

p = [2, 1, 3, 2]
l = 2
s = solution(p,l)
print(s)

