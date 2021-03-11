def solution(answers):
    answer = [0]*3
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
      
      if n1[i%len(n1)] == answers[i]:
        answer[0]+=1
      if n2[i%len(n2)] == answers[i]:
        answer[1]+=1
      if n3[i%len(n3)] == answers[i]:
        answer[2]+=1 
    a = []
    for i in range(3):
      if answer[i] == max(answer):
        a.append(i+1)


    return a

answers = [1,3,2,4,2]	
#가장 많은 문제를 맞힌 사람
s = solution(answers)
print(s)