# 점프와 순간이동
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12980

**문제 내용**  
OO 연구소는 한 번에 K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동을 할 수 있는 특수한 기능을 가진 아이언 슈트를 개발하여 판매하고 있습니다. 이 아이언 슈트는 건전지로 작동되는데, 순간이동을 하면 건전지 사용량이 줄지 않지만, 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다. 그러므로 아이언 슈트를 착용하고 이동할 때는 순간 이동을 하는 것이 더 효율적입니다. 아이언 슈트 구매자는 아이언 슈트를 착용하고 거리가 N 만큼 떨어져 있는 장소로 가려고 합니다. 단, 건전지 사용량을 줄이기 위해 점프로 이동하는 것은 최소로 하려고 합니다. 아이언 슈트 구매자가 이동하려는 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을 return하는 solution 함수를 만들어 주세요.

예를 들어 거리가 5만큼 떨어져 있는 장소로 가려고 합니다.
아이언 슈트를 입고 거리가 5만큼 떨어져 있는 장소로 갈 수 있는 경우의 수는 여러 가지입니다.

처음 위치 0 에서 5 칸을 앞으로 점프하면 바로 도착하지만, 건전지 사용량이 5 만큼 듭니다.
처음 위치 0 에서 2 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 2) x 2에 해당하는 위치로 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 3 만큼 듭니다.
처음 위치 0 에서 1 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동할 수 있으므로 위치 2로 이동됩니다. 이때 다시 순간이동 하면 (현재까지 온 거리 : 2) x 2 만큼 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 2 만큼 듭니다.
위의 3가지 경우 거리가 5만큼 떨어져 있는 장소로 가기 위해서 3번째 경우가 건전지 사용량이 가장 적으므로 답은 2가 됩니다.

**제한조건**  
- 숫자 N: 1 이상 10억 이하의 자연수
- 숫자 K: 1 이상의 자연수

**입출력 예**  
|n|result|
|------|---|
|5|2|
|6|2|
|5000|5|



**내가 푼 코드**  
```python
def solution(n):
    ans = 0
    while n!=0:
      if n%2 == 0:
        n = n//2
      else:
        n = n-1
        ans +=1      
    return ans
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
```


# 영어 끝말 잇기
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12981

**문제 내용**  
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
이전에 등장했던 단어는 사용할 수 없습니다.
한 글자인 단어는 인정되지 않습니다.
다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

tank → kick → know → wheel → land → dream → mother → robot → tank

위 끝말잇기는 다음과 같이 진행됩니다.

1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
(계속 진행)
끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

**제한조건**  
끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
단어의 길이는 2 이상 50 이하입니다.
모든 단어는 알파벳 소문자로만 이루어져 있습니다.
끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
정답은 [ 번호, 차례 ] 형태로 return 해주세요.
만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.

**입출력 예**  
|n|words|result|
|------|---|---|
|3|["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]|[3,3]|
|5|["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]|[0,0]|




**내가 푼 코드**  
```python
import collections

def solution(n, words):
    answer = []
    members = {i:[] for i in range(1,n+1)}

    for i,w in enumerate(words):
      if (i+1)%n==0:
        members[n].append(w)
        continue
      members[(i+1)%n].append(w)
    
    
    ch = words[0][0]
    al = []
    for i,word in enumerate(words):

      #한글자 인 경우
      if len(word)==1:
        return [(i+1)%n,(i//n)+1]
      #끝말로 안시작한경우
      if ch[-1] != word[0]:
        return [(i+1)%n,(i//n)+1]
      #나온글자 반복
      if word in al:
        if (i+1)%n == 0:
          return [n,(i//n)+1]
        return [(i+1)%n,(i//n)+1]
      
      al.append(word)
      ch = word

    return [0,0]
```
**코드 풀이 리뷰**  
왜 테케 4개가 안맞을까    
틀린사람 번호 구할때 (i+1)%n -> i%n+1로 변경 
   

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python
def solution(n, words):
    answer = [0, 0]
    count = 1 # range가 1부터 시작하므로, 1으로 설정 
    for idx in range(1, len(words)): # 1부터 시작하는 이유는 첫번째 사람의 첫 단어는 절대 틀릴 일이 없음 
        word = words[idx] # words[idx] : 언급된 단어 
        count %= n 
        if (word in words[0:idx]) or (words[idx-1][-1] != word[0]): 
            answer = [count +1, 1 + idx//n] #틀린사람번호, 몇번째 라운드 
            return answer 
        count +=1 
    return answer
```
굳이 collections.Counter를 이용해서 번호별로 안나눠줘도 되는 
더 간단한 풀이가 있었다.



# 배달
N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다. 다음은 N = 5, K = 3인 경우의 예시입니다.

위 그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 3 이하의 시간에 배달할 수 있습니다. 그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다. 따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.
마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.


**제한조건**  
- 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
- road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
- road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
- road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
-a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
- 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
- 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
- K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
- 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
- 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.


**입출력 예**  
|N|road|K|result|
|------|---|---|---|
|5|	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]|3|4|
|6|[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]|4|5|




**내가 푼 코드**  
```python
from collections import deque

def solution(N, road, K):
    nodes = {i:[] for i in range(1,N+1)}
    dist = {i:float('inf') if i!=1 else 0 for i in range(1,N+1)}
    #print(dict)
    for r in road:
      nodes[r[0]].append([r[1],r[2]])
      nodes[r[1]].append([r[0],r[2]])
    #print(nodes)


    queue = deque([1])
    while queue:
      cur_node = queue.popleft()
      for nxt_node,d in nodes[cur_node]:
        if dist[nxt_node]>dist[cur_node]+d:
          dist[nxt_node] = dist[cur_node]+d
          queue.append(nxt_node)
    
    return len([True for d in dist.values() if d<=K])
```
**코드 풀이 리뷰**  

   

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```
float()함수: 문자,문자열을 실수로 변경, 주로 변수에 아주 큰 값 할당해야 하는 경우 사용
float('inf') -> 양의 무한대
float('-inf') -> 음의 무한대



# 방문길이
https://programmers.co.kr/learn/courses/30/lessons/49994

게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기

D: 아래쪽으로 한 칸 가기

R: 오른쪽으로 한 칸 가기

L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.


**제한조건**  
dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
dirs의 길이는 500 이하의 자연수입니다.


**입출력 예**  
|dirs|answer|
|------|---|
|"ULURRDLLU"|7|
|"LULLLLLLU"|7|



**내가 푼 코드**  
```python
def solution(dirs):
    answer = 0
    roads = []
    road = []
    x,y = 0,0
    start = [x,y]

    for dir in dirs:
      if dir == 'U':
        y+=1
      if dir == 'D':
        y-=1
      if dir == 'R':
        x+=1
      if dir == 'L':
        x-=1

      if x<-5 or x>5 or y<-5 or y>5:
        x = start[0]
        y = start[1]
        continue

      road.append(start)
      road.append([x,y])#갱신후
      road.sort()
      if road not in roads:
        roads.append(road)
        
      start = [x,y] #갱신후로 start 바꾸기
      road = []

    return len(roads)



```
**코드 풀이 리뷰**  

  
**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  

```python

```
