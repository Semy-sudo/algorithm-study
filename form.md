# 문제명
문제 링크 : [문제링크]

**문제 내용**  
어떤 식당에서 둥근 테이블에 N명의 사람이 차례대로 1,2,..N번째 자리에 앉아있다. 각 사람들은 음식을 먹는 속도가 다르거나 같을 수 있으며,  
음식을 다 먹었어도 마주하게 앉은 사람이 나이가 더 많을 경우 그 사람이 다 먹을 때까지 앉아서 기다려야한다. 이때, K번째 음식을 먹는 손님이  
몇번째로 일어나는지를 return 하는 solution 함수를 완성해 주세요.

**제한조건**  
배열 p의 크기 : 1,000,000 이하의 자연수
배열 p의 원소의 크기 : 1보다 크거나 같고 보다 60보다 작거나 같은 정수

**입출력 예**  
input 
7
output
12

## 예시1  
**내가 푼 코드**  
둥근 테이블에 앉아 있는 손님들 중에서 K번째 음식을 먹는 손님을 알아내기 위해 원형큐로 구현했다.
그리고 음식을 다 먹은 손님들은 해시에 저장했는데, 해시를 사용했기 때문에 더 빠르게 다 먹은 손님을 알아낼 수 있다.
어쩌고 저쩌고. 전체적인 시간 복잡도는 이 부분을 이렇게 저렇게 계산하면 O(NlogN)이 나온다. 
이런식으로 접근해서 풀었는데 틀렸다.
```python
내가 푼 코드
```
**코드 풀이 리뷰**  
주어진 테스트 케이스의 경우는 잘 통과하는데 나머지 케이스에서 틀린다. 예를들어 9일 때는 11이 나오는데 왜 11이 나오는지 모르겠다 ㅠㅠ

**코드 리뷰**(코드 리뷰를 통해 해결했을 시)  
어쩌고 저쩌고한 케이스에서 예외처리를 하지 않아서 반례가 존재했다. flag를 써서 해당 부분을 체크하고 상태를 True로 바꿔준다.
```python
수정한 코드
```

## 예시2  
**내가 푼 코드**    
문제에서 이러이러한 부분은 브루트포싱을 통해 구현을 했는데 이 조건은 어떻게 구현해야할지 몰라서 하루종일 끄적였다. 너무 어렵다.
```python
내가 푼 코드
```  
**코드 풀이 리뷰**  
다른 사람 풀이를 찾아봤는데, 이런식으로 접근하더라. 그래서 일단 해당 개념에 맞춰서 다시 문제를 접근해보고 끄적여봤으나 막혔다.

**막힌 것**  
  1. 순차적으로 진행되는게 아니라 index를 왔다갔다해야하는데 어떻게 추적할지 몰라서 for문으로 삽질  
  2. 삽질시간이 길어지다보니 계속 오타내고 삽질
  
**코드 리뷰**  
index를 추적할 수 있도록 임의의 배열(arr)을 만들어서 bfs를 사용했다. 
```python
수정한 코드
```
**알게된 것**

**ㅁㅁ모듈의 ㅇㅇ메서드**  
숫자와 문자열이 있을 때 이러이러한 기능을 해서 이걸 반환해줌.
```python
>>> s = "1234 test"
>>> s.ㅇㅇ()
결과1
```
기존에는 이런저러한 방법으로 작성해야했지만,
```python
~~~대충 그런 코드
결과2
```
숫자가 들어올 경우 값이 이렇게 변환되기 때문에 안된다.
