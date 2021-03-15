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
