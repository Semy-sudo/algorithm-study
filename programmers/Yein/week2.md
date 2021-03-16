# 3진법 뒤집기 3진법 뒤집기
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/68935

**문제 내용**  
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

**제한조건**  
- n은 1 이상 100,000,000 이하인 자연수입니다.

**입출력 예**  
|n|result|
|------|---|
|45|7|
|125|229|




**내가 푼 코드**  
```python
def solution(n):
    answer = 0
    s = []
    #1. n-> 3진법으로 변환
    while True:
      s.append(n%3) 
      n = n//3
      if n==0:
        break
      
    for i,val in enumerate(reversed(s)):
      answer += val*(3**i)

    return answer
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
def solution(n):
  answer = []
  while True:
    n, rest = divmod(n,3)
    answer.append(rest)
    if n==0:
      break

  return sum([val*3**idx for idx,val in enumerate(reversed(answer))])
```
파이썬 내장함수중 divmod 함수를 이용:
* divmod(a,b)
매개변수로 a,b를 받아 a를 b로 나누고 그 (몫, 나머지) 튜플형태로 반환


# 완주하지 못한 선수
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42576
**문제 내용**  
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

**제한조건**  
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

**입출력 예**  
|participant|completion|return|
|------|---|---|
|["leo", "kiki", "eden"]|["eden", "kiki"]|"leo"|
|["marina", "josipa", "nikola", "vinko", "filipa"]|["josipa", "filipa", "marina", "nikola"]|"vinko"|

**내가 푼 코드**  
```python
def solution(participant, completion):
    answer = ''
    for person in participant:
      if person not in completion:
        answer = person 
        break
      completion.remove(person)
      
    return answer
```
**코드 풀이 리뷰**  
실행결과는 통과지만 효율성 테스트에서 전부 시간초과가 나왔다.
for 문에서 O(n) * if not in 에서 O(n) 시간 복잡도가 발생하였기 때문이라고 생각한다.

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
def solution(participant,completion):
  participant.sort()
  completion.sort()
  for p,c in zip(participant,completion):
    if p != c:
      return p
    
  return participant.pop()
```
1) sort 함수 정렬 -> participant와 completion에 해당 참가자가 같은 개수가 아닌 경우 찾아낼 수 있음 
2) zip() 내장함수 이용.
zip() 은 동일한 개수로 이루어진 자료형을 묶어 주는 역할
for문 하나로 비교

시간복잡도가 O(N)으로 줄어 통과할 수 있었다

# 다트게임
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17682
**문제 내용**  
카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.
갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.

다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

**제한조건**  
입력 형식
"점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
예) 1S2D*3T

점수는 0에서 10 사이의 정수이다.
보너스는 S, D, T 중 하나이다.
옵선은 *이나 # 중 하나이며, 없을 수도 있다.
출력 형식
3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
예) 37

**입출력 예**  
|예제|darkResult|answer|설명|
|------|---|---|---|
|1|1S2D*3T|39| (1^1 * 2) + (2^2 * 2) + (3^3) |
|2|1D2S#10S|9|---|
|3|1D2S0T|3|---|

**내가 푼 코드**  
```python
def solution(dartResult):
    bonus = {'S':1,'D':2,'T':3}
    option = {'*':2,'#':-1,'':1}
    #정규 표현식
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] =='*' and i>0:
            dart[i-1] *=2
        dart[i] = int(dart[i][0])**bonus[dart[i][1]]*option[dart[i][2]]
        print(dart)
    answer=sum(dart)
    return answer
```
**코드 풀이 리뷰**  
정규표현식을 안쓰니 문제가 안풀려서, 문자열을 숫자|문자|문자 로 구분해 리스트에 담아주는 정규표현식을 사용.
- [('1', 'S', ''), ('2', 'T', ''), ('3', 'S', '')]

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```
- 실패율규표현식을 안쓰니 문제가 안풀려서, 문자열을 숫자|문자|문자 로 구분해 리스트에 담아주는 정규표현식을 사용.
 [('1', 'S', ''), ('2', 'T', ''), ('3', 'S', '')]


# 실패율

문제 링크 : 
https://programmers.co.kr/learn/courses/30/lessons/42889

**문제 내용**  
슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

**제한조건**  
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

**입출력 예**  
|N|stages|result|
|------|---|---|
|5|[2,1,2,6,2,4,3,3]|[3,4,2,1,5]|
|4|[4,4,4,4,4]|[4,1,2,3]|

**내가 푼 코드**  
```python
def solution(N, stages):
    answer = []
    lis = {i:'' for i in range(1,N+1)}

    sum = 0
    for i in range(1,n+1):
      lis[i] = stages.count(i)/(len(stages)-sum)
      sum += stages.count(i)
    
    lis = sorted(lis.items(), key=lambda x:x[1], reverse=True)
    for i in lis:
      answer.append(i[0])

    return answer
```
```python
def solution(N, stages):
    answer = []
    lis = {i:'' for i in range(1,N+1)}

    sum = 0
    for i in range(1,N+1):
      m = len(stages)-sum
      if m==0:
        lis[i] = stages.count(i)/1
      else:
        lis[i] = stages.count(i)/m
      sum += stages.count(i)
    
    lis = sorted(lis.items(), key=lambda x:x[1], reverse=True)
    for i in lis:
      answer.append(i[0])


    return answer
```

**코드 풀이 리뷰** 

런타임에러
- 배열에 할당된 크기를 넘어서 접근했을 때
- 전역 배열의 크기가 메모리 제한을 초과할 때
- 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
- 0으로 나눌 떄
- 라이브러리에서 예외를 발생시켰을 때
- 재귀 호출이 너무 깊어질 때
- 이미 해제된 메모리를 또 참조할 때

0으로 나눠지지 않게 조건문 설정

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```