# 튜플
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

**문제 내용**  
예를 들어 입력으로 KAKAO가 들어온다고 하자.

현재 사전에는 KAKAO의 첫 글자 K는 등록되어 있으나, 두 번째 글자까지인 KA는 없으므로, 첫 글자 K에 해당하는 색인 번호 11을 출력하고, 다음 글자인 A를 포함한 KA를 사전에 27 번째로 등록한다.
두 번째 글자 A는 사전에 있으나, 세 번째 글자까지인 AK는 사전에 없으므로, A의 색인 번호 1을 출력하고, AK를 사전에 28 번째로 등록한다.
세 번째 글자에서 시작하는 KA가 사전에 있으므로, KA에 해당하는 색인 번호 27을 출력하고, 다음 글자 O를 포함한 KAO를 29 번째로 등록한다.
마지막으로 처리되지 않은 글자 O에 해당하는 색인 번호 15를 출력한다.

(a1, a2, a3, ..., an)
튜플은 다음과 같은 성질을 가지고 있습니다.

중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
튜플의 원소 개수는 유한합니다.
원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.

{{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
예를 들어 튜플이 (2, 1, 3, 4)인 경우 이는

{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
와 같이 표현할 수 있습니다. 이때, 집합은 원소의 순서가 바뀌어도 상관없으므로

{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
{{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}
는 모두 같은 튜플 (2, 1, 3, 4)를 나타냅니다.

특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

**제한조건**  
s의 길이는 5 이상 1,000,000 이하입니다.
s는 숫자와 '{', '}', ',' 로만 이루어져 있습니다.
숫자가 0으로 시작하는 경우는 없습니다.
s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수입니다.
return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다

**입출력 예**  
|s|result|
|------|---|
|"{{2},{2,1},{2,1,3},{2,1,3,4}}"|[2, 1, 3, 4]|




**내가 푼 코드**  
```python
def solution(s):
    answer = []
    s = s[2:-2] #문자열 분리
    s = s.split("},{") #str -> list
    s.sort(key=len)
    for i in s:
      i = i.split(",")
      for j in i:
        if int(j) not in answer:
          answer.append(int(j))

    return answer
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```
# 수식 최대화
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

**문제 내용**  


**제한조건**  


**입출력 예**  
|s|result|
|------|---|
|"{{2},{2,1},{2,1,3},{2,1,3,4}}"|[2, 1, 3, 4]|




**내가 푼 코드**  
```python

```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n+1, e) for e in expression.split('*')]))
        print("*",res)
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e) for e in expression.split('+')]))
        print("+",res)
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e) for e in expression.split('-')]))
        print("-",res)
    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))
    
    return answer

```


# 뉴스 클러스터링
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3



**문제 내용**  
기사의 제목을 기준으로 "블라인드 전형"에 주목하는 기사와 "코딩 테스트"에 주목하는 기사로 나뉘는 걸 발견했다. 튜브는 이들을 각각 묶어서 보여주면 카카오 공채 관련 기사를 찾아보는 사용자에게 유용할 듯싶었다.

유사한 기사를 묶는 기준을 정하기 위해서 논문과 자료를 조사하던 튜브는 "자카드 유사도"라는 방법을 찾아냈다.

자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

예를 들어 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때, 교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로, 집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다. 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.

자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다. 다중집합 A는 원소 "1"을 3개 가지고 있고, 다중집합 B는 원소 "1"을 5개 가지고 있다고 하자. 이 다중집합의 교집합 A ∩ B는 원소 "1"을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 "1"을 max(3, 5)인 5개 가지게 된다. 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면, 교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로, 자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다.

이를 이용하여 문자열 사이의 유사도를 계산하는데 이용할 수 있다. 문자열 "FRANCE"와 "FRENCH"가 주어졌을 때, 이를 두 글자씩 끊어서 다중집합을 만들 수 있다. 각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며, 교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로, 두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH") = 2/8 = 0.25가 된다.

**제한조건**  
입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.

**입출력 예**  
|str1|str2|answer
|------|---|---|
|FRANCE|french|16384|




**내가 푼 코드**  
```python
import re
import collections
import math

def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
      if str1[i:i+2].isalpha():
        s1.append(str1[i:i+2].upper())
    for i in range(len(str2)-1):
      if str2[i:i+2].isalpha():
        s2.append(str2[i:i+2].upper())

    f1 = []#교집합
    f2 = []#합집합
    s1 = collections.Counter(s1)
    s2 = collections.Counter(s2)
    
    if not len(s1) and not len(s2):
      return 65536 
    else:
      answer = math.trunc((len(s1 & s2)/len(s1 | s2))*65536)
      return answer
```
**코드 풀이 리뷰**  
"aa1+aa2", "AAAA12"입력값이 주어질때
오류 - 실행한 결괏값 65536이(가) 기댓값 43690와(과) 다릅니다.



**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
import re
import math

def solution(str1, str2):
    # 두칸씩 쪼갠 값이 모두 문자이면 str1, str2에 append 
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    # 합집합과 교집합 계산 
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    # 합집합이 0이면 65536 출력 
    if len(hap) == 0 :
        return 65536

    # 교집합하고 합집합의 counter를 따로 계산
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])
    

    return math.floor((gyo_sum/hap_sum)*65536)
```
1. 기존방식대로 중복을 포함하지 않고 합,교 집합을 &,|로 구한다.
2. 합집합의 경우 각 리스트의 원소에서 최솟값으로 바꿔주고, 교집합의 경우에는 리스트의 원소의 최댓값들을 다 더한다.

# 프렌즈4블록
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17679

**문제 내용**  
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

**제한조건**  


**입출력 예**  
|m|n|s|result|
|------|---|---|---|
|4|5|["CCBDE", "AAADE", "AAABF", "CCBBF"]|14|




**내가 푼 코드**  
```python
def erase_block(asnwer,board,i,j):
  dx_lh = [0,1,1]
  dy_lh = [1,0,1]
  dx_rh = [-1,-1,0]
  dy_rh = [0,1,1]
  dx_ld = [1,1,0]
  dy_ld = [-1,0,-1]
  dx_rd = [-1,-1,0]
  dy_rd = [0,-1,-1]
  #lh 가 없어지는 상황
  ans = [] #지울때 중복없게 후보 넣어둠
  ans.append([i,j])
  if board[i][j]==board[i+dx_lh[0]][j+dy_lh[0]]==board[i+dx_lh[1]][j+dy_lh[1]]==board[i+dx_lh[2]][j+dy_lh[2]]:
    for i in range(3):
      if [dx_lh[i],dy_lh[i]] not in ans:
        ans.append([dx_lh[i],dy_lh[i]])

  #rh
  if board[i][j]==board[i+dx_rh[0]][j+dy_rh[0]]==board[i+dx_rh[1]][j+dy_rh[1]]==board[i+dx_rh[2]][j+dy_rh[2]]:
    for i in range(3):
      if [dx_rh[i],dy_rh[i]] not in ans:
        ans.append([dx_rh[i],dy_rh[i]])

  #ld
  if board[i][j]==board[i+dx_ld[0]][j+dy_ld[0]]==board[i+dx_ld[1]][j+dy_ld[1]]==board[i+dx_ld[2]][j+dy_ld[2]]:
    for i in range(3):
      if [dx_ld[i],dy_ld[i]] not in ans:
        ans.append([dx_ld[i],dy_ld[i]])

  #rd
  if board[i][j]==board[i+dx_rd[0]][j+dy_rd[0]]==board[i+dx_rd[1]][j+dy_rd[1]]==board[i+dx_rd[2]][j+dy_rd[2]]:
    for i in range(3):
      if [dx_rd[i],dy_rd[i]] not in ans:
        ans.append([dx_rd[i],dy_rd[i]])

  answer = len(ans)
  #board 변경
  #ans = [[1,2],[1,1]...]
  m_y = []
  m_x = []
  for i in range(len(ans)):
    m_y.append(ans[i][1])
  for i in range(len(ans)):
    m_x.append(ans[i][0])
  for k in range(max(m_y)+1,len(board)):
    for x in m_x:
      board[k-2][x] = board[k][x]


  #변경된 board로 다시 시작
  change(asnwer,board)

    
  return answer

def change(asnwer,board):
  for i in range(m-1):
        for j in range(n-1):
          erase_block(asnwer,board,i,j)

def solution(m, n, board):
    answer = 0
    num = {i:[] for i in range(m)}
    for i,b in enumerate(board):
      for bb in b:
        num[i].append(bb)
    print(num)
    #r_h,l_h,r_d,l_d
    answer = change(answer,board)

    return answer
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
def pop_num(b,m,n):
  pop_set = set()
  for i in range(1,n):
    for j in range(1,m):
      if b[i][j]==b[i][j-1]==b[i-1][j-1]==b[i-1][j] != '_':
        pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)]) #없어질 좌표값 넣어주기

  #set_board 
  for y,x in pop_set:
    b[y][x] = 0
  for i,row in enumerate(b):
    empty = ['_']*row.count(0)
    b[i] = empty+[block for block in row if block!=0]
  return len(pop_set)

def solution(m, n, board):
    count = 0
    b = list(map(list,zip(*board)))
    print(b)
    while True:
        pop = pop_num(b, m, n)
        if pop == 0: return count
        count += pop
```
1. 좌표값 중복방지를 위해서 pop_set = set() 자료형으로 만들기
2. a |=b : a or b 연산을 하여 a에 값 넣어주기
3. empty = 현재 row에서 0의 개수
기존의 0이아닌 block과 합쳐줌 

# 캐시      
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17680

**문제 내용**  
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

**제한조건**  
캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
cache hit일 경우 실행시간은 1이다.
cache miss일 경우 실행시간은 5이다.

**입출력 예**  
|catchsize|cities|result|
|------|---|---|---|
|3|["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]|50|




**내가 푼 코드**  
```python
def solution(cacheSize, cities):
    answer = 0
    st = []
    if cacheSize==0:
      return len(cities)*5
    for city in cities:
      city = city.upper()
      if len(st)<cacheSize and city not in st:
        st.append(city)
        answer +=5
        continue
      if city not in st:
        st.remove(st[0])
        st.append(city)
        answer +=5
        continue
      else:
        st.remove(city)
        st.append(city)
        answer +=1
        
    return answer
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```

# 방금그곡      
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17683

**문제 내용**  
라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다. 그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다. 그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다. 반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다. 그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
음악이 00:00를 넘겨서까지 재생되는 일은 없다.
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

**제한조건**  
m은 음 1개 이상 1439개 이하로 구성되어 있다.
musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.
음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.

**입출력 예**  
|catchsize|cities|result|
|------|---|---|---|
|"ABCDEFG"|["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]|"HELLO"|




**내가 푼 코드**  
```python
def change(melody):
    if 'A#' in melody: melody = melody.replace('A#','a')
    if 'C#' in melody: melody = melody.replace('C#','c')
    if 'D#' in melody: melody = melody.replace('D#','d')
    if 'F#' in melody: melody = melody.replace('F#','f')
    if 'G#' in melody: melody = melody.replace('G#','g')
    return melody

def solution(m, musicinfos):
  m = change(m)
  answer = ('(None)',None) #제목, 시간
  for info in musicinfos:
    start, end, title, melody = info.split(',')
    start_h,start_m,end_h,end_m = map(int,start.split(':')+end.split(':'))
    time = (end_h-start_h)*60+end_m-start_m
    melody = change(melody)
    realmelody = (melody*time)[:time]
    if m in realmelody:
      if answer[1]==None or answer[1]<time:
        answer = (title,time)

  return answer[0]
```
**코드 풀이 리뷰**  
G#과 같이 #이붙은 알파벳도 1분 수행시간이기 때문에
[:time] 으로 해당 시간만큼 멜로디길이를 잘라줄때
문제가 될수 있기 때문에 소문자로 변경했다

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```




# 압축
문제링크
https://programmers.co.kr/learn/courses/30/lessons/17684


**문제 내용**  
현재 사전에는 KAKAO의 첫 글자 K는 등록되어 있으나, 두 번째 글자까지인 KA는 없으므로, 첫 글자 K에 해당하는 색인 번호 11을 출력하고, 다음 글자인 A를 포함한 KA를 사전에 27 번째로 등록한다.
두 번째 글자 A는 사전에 있으나, 세 번째 글자까지인 AK는 사전에 없으므로, A의 색인 번호 1을 출력하고, AK를 사전에 28 번째로 등록한다.
세 번째 글자에서 시작하는 KA가 사전에 있으므로, KA에 해당하는 색인 번호 27을 출력하고, 다음 글자 O를 포함한 KAO를 29 번째로 등록한다.
마지막으로 처리되지 않은 글자 O에 해당하는 색인 번호 15를 출력한다.

**제한조건**  
입력으로 영문 대문자로만 이뤄진 문자열 msg가 주어진다. msg의 길이는 1 글자 이상, 1000 글자 이하이다.

**입출력 예**  
|msg|result|
|------|---|
|"KAKAO"|[11, 1, 27, 15]|


**내가 푼 코드**  
```python
def find(msg,dic):
  for i in range(1,len(msg)+1):
    if msg[:i] in dic:
      w = msg[:i]
    else:
      return w
  return w

def solution(msg):
    answer = []
    dic1 = ['0']
    #1.사전 만들기
    dic = [chr(c) for c in range(ord('A'), ord('Z')+1)] #ord-아스키값 돌려주는 함수
    dic = dic1 + dic #번호와 알파벳을 맞춰주기 위해
  
    #2.찾기
    while msg:
      w = find(msg,dic) #msg에서 w 찾기
      if msg == w:
        answer.append(dic.index(w))
        return answer
      msg = msg[len(w):]
      c = msg[0]
    
      dic.append(w+c)
      answer.append(dic.index(w))

    return answer
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```

# 파일명저장
문제링크
https://programmers.co.kr/learn/courses/30/lessons/17686

**문제 내용**  
소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.

파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.

HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.

**제한조건**  
파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 이때, 문자열 비교 시 대소문자 구분을 하지 않는다. MUZI와 muzi, MuZi는 정렬 시에 같은 순서로 취급된다.
파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다. 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다. 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.
두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다

**입출력 예**  
입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]


**내가 푼 코드**  
```python
import re

def solution(files):
    answer = []
    new_files = []
    for i,f in enumerate(files):
      number = re.findall("\d+",f)
      number[0]#12, 02
      second = int(number[0])#숫자
      first = f[0:f.index(number[0][0])].upper()#숫자앞문자
      last = f[f.index(number[0][-1])+1:]#나머지
      new_files.append([i,first,second,last])
    #head가 같을경우number숫자순
    new_files = sorted(new_files, key=lambda x:x[2])

    #head로 정렬
    new_files = sorted(new_files, key=lambda x:x[1])

    #출력
    for n in new_files:
      answer.append(files[n[0]])

    
    return answer
```
**코드 풀이 리뷰**  
1. re.findall("\d+",f) - 문자열f에서 숫자에 해당하는 부분찾아 배열로 반환 단, 연속적인 숫자는 붙여서 하나의 value만듬

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```