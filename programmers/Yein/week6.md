# 기능개발 
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42586

**문제 내용**  


**제한조건**  

**입출력 예**  
input
[93, 30, 55]
output
[1, 30, 5]

**내가 푼 코드**  
```python
def solution(progresses, speeds):
    answer = []
    st = []
    for i,p in enumerate(progresses):
      if (100-p)%speeds[i]!=0:
        st.append((100-p)//speeds[i]+1)
      else:
        st.append((100-p)//speeds[i])
    
    print(st)
    pick = st[0]
    t = 1
    # pick을 기준으로 pick보다 커지지 않을때까지 t를 증가시킴
    while(len(st)>0):
      if len(st)==1:
        answer.append(t)
        break
      st = st[1:]
      if pick<st[0]:
        answer.append(t)
        t = 1
        pick = st[0]
      else: #pick 이 변하지 않음
        t+=1


    return answer
```
**코드 풀이 리뷰**  
조건에 따라 배열을 파싱하여 배열의 첫번째 값과 비교

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
def solution(progresses, speeds):
    Q = []
    for p,s in zip(progresses,speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1


    return [q[1] for q in Q]
```
//는 내림하여 결과가 반환됨
- -70//2 = -3
- 70//2 = 2

굉장히 간단한 풀이를 발견했다.
2차원 배열을 이용하여 Q[비교할숫자,증가값] 을 만듬

# 프린터
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42587

**문제 내용**  


**제한조건**  

**입출력 예**  
input
p = [2, 1, 3, 2] l = 2
output
1

**내가 푼 코드**  
```python

```
**코드 풀이 리뷰**  

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
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
```
찾아야 하는 값의 위치값도 계속 변경해 주면서 
순서가 왔을때(스택에서 최댓값이 되었을때) 몇번째로 그 순서가
왔는지 구해주는 방식
