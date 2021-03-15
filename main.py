def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    #참가자는 2명인데 c에 1명만 있을 때
    for p,c in zip(participant, completion):
      if p != c:
        
        return p


#참가자중 c에 없을때 
    return participant.pop()


participant = ["marina", "josipa", "marina", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina","vinko"]
s = solution(participant,completion)
print(s)


  