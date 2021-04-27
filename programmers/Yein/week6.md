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
# 주식가격
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

**문제 내용**  


**제한조건**  

**입출력 예**  
input
[1, 2, 3, 2, 3]
output
[4, 3, 1, 1, 0]

**내가 푼 코드**  
```python
def solution(prices):
    answer = [0]*len(prices)
    for i,p in enumerate(prices):
      new_prices = prices[i+1:]
      for np in new_prices:
        answer[i]+=1
        if p>np:#가격이 떨어졌으면
          break

    return answer
```
**코드 풀이 리뷰**  
정확성 테스트는 맞는데 효율성 테스트에서 통과가 안된다.
아무래도 이중 for문을 사용하여 그런것 같다.

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)]#주식가격 떨어지는 시점 정보
    st = [0]#인덱스를 차례로 담아두는 배열
    for i in range(1,len(prices)):
      while st:
        if prices[st[-1]]>prices[i]:#가격이 떨어졌으면
          answer[st[-1]] = i-st[-1]#해당 인덱스의 주식가격 떨어지는 시점 정보 변경
          st.pop()#결정된 인덱스 버림
        else:
          break #더이상 더 낮은 가격이 없으면 멈춤
      st.append(i)#다음 가격과 비교를 위해 현재 인덱스 넣어둠

    return answer
```
- stack 을 이용
먼저 가격이 떨어지는 배열을 기본 세팅해놓고 answer = [4,3,2,1,0]
이중에서 주식가격이 떨어져 가격이 일찍 바뀌는 인덱스만 변경해주는 로직

변경시 현재시점과 스택에 담겨있는 과거의 인덱스들을 비교하여 가격이 떨어졌으면 현재인덱스- 과거인덱스 하여 answer다시세팅


# 다리를 지나는 트럭
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42583

**문제 내용**  



**제한조건**  

**입출력 예**  
input
2 10
output
[7,4,5,6]

**내가 푼 코드**  
```python
def solution(bridge_length, weight, truck_weights):
    answer = 0 #time
    end_t = [] #다리를 다 건넌 트럭
    mid_t = [0]*(bridge_length) #다리를 건너는 중인 트럭으로 weight,length넘으면 안됨
    
    while(len(truck_weights)>0):
      #mid_t => end_t
      if mid_t[0]!=0:
        end_t.append(mid_t[0])
      mid_t = mid_t[1:]+[0]
   
      #truck_weights => mid_t
      if sum(mid_t)+truck_weights[0]<=weight:
        t = truck_weights.pop(0)
        mid_t[-1] = t
      
      answer+=1

    for i,m in enumerate(reversed(mid_t)):
      if m!=0:
        remain = bridge_length-i
        break
        
    return answer+remain
```
**코드 풀이 리뷰**  
테게 5에서 시간초과로 실패가 떳다
푸는데 꽤 오래 걸렸던것 같다ㅜㅜ
시간적 순서 반대로 코드를 짜주어야 하는데 그부분에서 많이
헷갈렸다.

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0]*bridge_length

    while q:
      time +=1
      q.pop(0)# 맨앞의 큐의 원소가 없어지고
      if truck_weights:
        if sum(q)+truck_weights[0]<=weight:#조건이 맞으면
          q.append(truck_weights.pop(0))#새로운 트럭이 들어올 수 있음
        else:
          q.append(0)#조건이 안맞으면 길이 맞추기 위해 0삽입

    return time
```
다리를 건너는 트럭 = q[] 를 기준으로 time을 설정해줌
q 에 트럭이 다 지나가게 되면 len(truck_weights)가 0이 되기 때문에 q는 계속하여 pop된다.


# 삼각 달팽이   return time
```
다리를 건너는 트럭 = q[] 를 기준으로 time을 설정해줌
q 에 트럭이 다 지나가게 되면 len(truck_weights)가 0이 되기 때문에 q는 계속하여 pop된다.


# 삼각 달팽이
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42583

**문제 내용**  

문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42583

**문제 내용**  



**제한조건**  

**입출력 예**  
input
2 10
output
[7,4,5,6]

**내가 푼 코드**  
```python

```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```

```
