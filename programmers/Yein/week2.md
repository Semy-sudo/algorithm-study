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

# 키패드 누르기

문제 링크 : 
https://programmers.co.kr/learn/courses/30/lessons/42889


**문제 내용**  
이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

**제한조건**

- numbers 배열의 크기는 1 이상 1,000 이하입니다.
- numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
- hand는 "left" 또는 "right" 입니다.
  - "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
- 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

**입출력 예**  
|numbers|hand|result|
|------|---|---|
|[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]|"right"|"LRLLLRLLRRL"|

**내가 푼 코드**  
```python
def find(n,p):
  key = [
      [1,2,3],
      [4,5,6],
      [7,8,9],
      ['*',0,'#']
  ]
  k = 0
  for arr in key:
    if n in arr:
      t = arr.index(n)
      break
    k+=1
  p = [k,t] #1,0
  return p

def solution(numbers, hand):
    answer = ''
    p_l =  [3,0]
    p_r = [3,2]
    p = []
    for n in numbers:
      if n==1 or n==4 or n==7:
        answer +='L'
        #왼쪽 키패드의 위치
        p_l = find(n,p_l) #1,0

      elif n==3 or n==6 or n==9:
        answer +='R'
        #오른쪽 키패드의 위치
        p_r = find(n,p_r) #1,0

      else:
        p = find(n,p)
        if abs(p_r[0]-p[0])+abs(p_r[1]-p[1]) > abs(p_l[0]-p[0])+abs(p_l[1]-p[1]):
          answer += 'L'
          p_l = p
        elif abs(p_r[0]-p[0])+abs(p_r[1]-p[1])< abs(p_l[0]-p[0])+abs(p_l[1]-p[1]):
          answer += 'R'
          p_r = p
        else:
          if hand == "right":
            h = 'R'
            answer += h
            p_r = p
          elif hand == "left":
            h = 'L'
            answer += h
            p_l = p

    return answer
```

**코드 풀이 리뷰** 
- numbers를 돌면서 해당 키패드의 위치 찾아줌

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```

# 소수 만들기

문제 링크 : 
https://programmers.co.kr/learn/courses/30/lessons/12977


**문제 내용**  
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

**제한조건**

- nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
- nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

**입출력 예**  
|nums|result|
|------|---|
|[1,2,3,4]|1|
|[1,2,7,6,4]|4|

**내가 푼 코드**  
```python
from itertools import combinations

def solution(nums):
    answer = len(list(combinations(nums, 3)))
    for l in list(combinations(nums, 3)):
      for i in range(2,sum(l)):
        if sum(l) % i == 0:
          answer -=1
          break
      
    return answer
```

**코드 풀이 리뷰** 
- combinations(nums,3) : nums에서 3개쌍 조합

- 2부터 sum(l)-1까지 수로 나눴을때 하나라도 0이 나오면 소수가 아님

  > 처음에는 sum(l) %2 !=0 and sum(l) %3 !=0 필터로 소수점을 찾을수 있을 거라 생각했다
조건이 10 이하 자연수가 아니기 때문에 틀린 생각이었다.

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```
# 크래인 인형뽑기 게임

문제 링크 : 
https://programmers.co.kr/learn/courses/30/lessons/64061

**문제 내용**  
게임개발자인 "죠르디"는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
"죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

crane_game_101.png

게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 "5 x 5" 크기의 예시입니다). 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다. 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다. 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.

crane_game_102.png

만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 두 개가 없어집니다.

crane_game_103.gif

크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.


**제한조건**

- board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
- board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
  - 0은 빈 칸을 나타냅니다.
  - 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
- moves 배열의 크기는 1 이상 1,000 이하입니다.
- moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

**입출력 예**  
|board|moves|result|
|------|---|
|[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]|[1,5,3,5,1,2,1,4]|4|

**내가 푼 코드**  
```python
## 스택사용
class Stack:
    def __init__(self): 
        self.top = [] # list-based stack
    def isEmpty(self):
        return len(self.top) == 0 # Empty list's length = 0
    def peek(self):
        if not self.isEmpty():
            return self.top[-1] # pos = -1 means 'last ite
    def pop(self):  # remove the top element of the Stack
        if not self.isEmpty(): # pop if stack is NOT EMPTY
            return self.top.pop(-1)  # pop(-1) : returns the last item of the list
        else:
            print("Stack underflow") 
            exit()
    def push(self, item): # add an element on the top of the Stack
        self.top.append(item)
            



def solution(board, moves):
    answer = 0
    st = []
    st2 = Stack()
    for item in moves:
      for i in range(len(board)):
        if board[i][item-1] !=0 :
          st.append(board[i][item-1])
          board[i][item-1] = 0
          break
    print(st)
    for i in range(len(st)):
      num = st.pop()
      
      if st2.peek() != num:
        st2.push(num)
      else:
        st2.pop()
        answer +=2
        

    return answer

    ## stack 클래스 안쓰고

def solution(board, moves):
    answer = 0
    st = []
    st2 = []
    for item in moves:
      for i in range(len(board)):
        if board[i][item-1] !=0 :
          st.append(board[i][item-1])
          board[i][item-1] = 0
          break
    for i in range(len(st)):
      num = st.pop()
      if len(st2)==0:
        st2.append(num)
      elif st2[-1] != num:
        st2.append(num)
      else:
        st2.pop()
        answer +=2
        

    return answer
```

**코드 풀이 리뷰** 
- 리스트를 두개 만들어 스택으로 활용
- st 에서 st2로 이동하면서 같은값 검사

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
def solution(board, moves):
    answer = 0
    st = []
    for item in moves:
      for i in range(len(board)):
        if board[i][item-1] !=0 :
          st.append(board[i][item-1])
          board[i][item-1] = 0
          if st[-1:] == st[-2:-1]:
            answer +=2
            st = st[:-2]
          break
    return answer

```
애초에 버킷에 넣을때 마지막 값과 비교하여 처리하는 로직

# 신규 아이디 추천

문제 링크 : 
https://programmers.co.kr/learn/courses/30/lessons/72410

**문제 내용**  
카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어, 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다. "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
다음은 카카오 아이디의 규칙입니다.

아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
"네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
신규 유저가 입력한 아이디가 new_id 라고 한다면,

---
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다. 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

---

신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.

**제한조건**

- new_id는 길이 1 이상 1,000 이하인 문자열입니다.
- new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
- new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.

**입출력 예**  
|new_id|result|
|------|---|
|"...!@BaT#*..y.abcdefghijklm"|"bat.y.abcdefghi"|

**내가 푼 코드**  
```python

def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    for word in new_id:
      if word.isalnum() or word in '_-.':
        answer += word

    #3
    while '..' in answer:
      answer = answer.replace('..','.')

    #4
    answer = answer[1:] if answer[0]=='.' and len(answer)>1 else answer
    answer = answer[:-1] if answer[-1] =='.' else answer

    #5
    answer = 'a' if answer=='' else answer

    #6
    if len(new_id)>=16:
      answer = answer[:15]
      if answer[-1]=='.':
        answer = answer[:-1]
    #7
    if len(answer)<3:
      answer = answer + answer[-1]*(3-len(answer))

    return answer


```
2번조건에서 정규식을 표현해야 하는줄 알고 시간을 많이 썻다
- answer = re.sub("[^a-z0-9-_.]","",new_id)
isalnum() 함수를 통해 숫자+영 조합인지, 정규식 말고 in '_-.'을 통해 걸러낼수 있다.

**코드 풀이 리뷰** 


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python



