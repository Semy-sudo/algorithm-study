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
        return [i%n+1,(i//n)+1]
      #끝말로 안시작한경우
      if ch[-1] != word[0]:
        return [i%n+1,(i//n)+1]
      #나온글자 반복
      if word in al:
        return [i%n+1,(i//n)+1]
      
      al.append(word)
      ch = word
 
    return [0,0]