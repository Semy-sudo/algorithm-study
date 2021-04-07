# 두개뽑아서 더하기
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

**문제 내용**  


**제한조건**  

**입출력 예**  
input
[2,1,3,4,1]	
output
[2,3,4,5,6,7]

**내가 푼 코드**  
```python
def solution(numbers):
    answer = []
    #두개뽑아 합 , 오름차순
    for i in range(len(numbers)-1):
      for j in range(i+1,len(numbers)):
        if (numbers[i]+numbers[j]) not in answer:
          answer.append(numbers[i]+numbers[j])

    answer.sort()
    return answer
```
**코드 풀이 리뷰**  
for문 2개 사용하면서도 계속 찝찝했음
다른 내장함수들을 사용할수 있는 방법이 있는지 고민

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
from itertools import combinations
def solution(numbers):
  answer = set()#중복허용안함
  for i in list(combinations(numbers,2)):
    answer.add(sum(i))
  return sorted(answer)
```

```
from itertools import combinations
def solution(numbers):
  return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,2)])))
```
- 파이썬 기본 라이브러리인 itertools의 combinations 라는 내장함수를 사용하여 인자값에 따라 해당 요소로 구할 수 있는 모든 조합을 리턴한다.
- combinations(numbers,2) = numbers리스트안에 2개 요소로 구할수 있는 모든 조합을 반환

# 베스트앨범
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42579

**문제 내용**  


**제한조건**  

**입출력 예**
input
[2,1,3,4,1]	
output
[2,3,4,5,6,7]

**내가 푼 코드**  
```python

```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
from collections import defaultdict
def solution(genres, plays):
    answer = []
    genres_dic = defaultdict(lambda: 0)#장르순서 저장 (장르:앨범개수)
    total_dic = defaultdict(lambda: [])#장르별 앨범개수,순서
    for i in range(len(plays)):
        genres_dic[genres[i]]+=plays[i]#{(classic:1231),(pop:452)}
        total_dic[genres[i]].append((plays[i],i))#{("classic":(500,0),(400,2),(  )  }
    
    genres_dic = sorted(genres_dic.items(),key = lambda x:x[1],reverse=True)
    for t in total_dic:
        total_dic[t] = sorted(total_dic[t],key = lambda x:x[0],reverse=True)[:2]
        
    print(genres_dic)
    print(total_dic)
    while len(genres_dic)>0:
        first = genres_dic.pop(0)
        for t in total_dic:
            if t==first[0]:
                if len(total_dic[t])>1:
                    answer.append(total_dic[t][0][1])
                    answer.append(total_dic[t][1][1])
                else:
                    answer.append(total_dic[t][0][1])
                    
```

- defaultdict(lambda: 0) -> 디폴트값이 0
- defaultdict(lambda: []) -> 디폴트값이 리스트

- list 변경하려면 -> list.sort()
- list로 새로운 정렬기준적용 리스트 생성하려면 -> list2 = sorted(list, 기준값 key=  , reverse=)

- 딕셔너리 dic = {"yello":4,"orange":5} -> dic.items() = {('yello',4),('orange',5)} key,value를 튜플형태로 묶어줌 

# 네트워크
문제 링크 :https://programmers.co.kr/learn/courses/30/lessons/43162


**문제 내용**  


**제한조건**  

**입출력 예**
input
	
output


**내가 푼 코드**  
```python
def stack(i,j,computers):
  st = []
  visited = []
  st.append([i,j])
  visited.append([i,j])

  while st:
    a,b = st.pop()
    for i in range(len(computers)):
      if [b,i] not in visited and computers[b][i]==1:
        visited.append([b,i])
        st.append([b,i])
        computers[b][i]=0
        

def solution(n, computers):
    answer = 0
   
    for i in range(len(computers)):
      for j in range(len(computers)):
        if computers[i][j]==1:
          stack(i,j,computers)
          answer +=1

        

    return answer
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```
```
# 같은 숫자는 싫어
문제 링크 :https://programmers.co.kr/learn/courses/30/lessons/12906


**문제 내용**  


**제한조건**  

**입출력 예**
input
[1,1,1,,0,3,3,1,1]	
output
[1,0,3,1]

**내가 푼 코드**  
```python
def solution(arr):
  answer = []
  for a in arr:
    if not answer:
      answer.append(a)
    if answer[-1] == a:
      continue
    answer.append(a)
  return answer
```
**코드 풀이 리뷰**  


**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
```python
def solution(arr):
    a = []
    for i in arr:
        print(a[-1:])
        if a[-1:] == [i]: continue
        a.append(i)
    return a

```


