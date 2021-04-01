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

    #순서로 files참조
    for n in new_files:
      answer.append(files[n[0]])

    
    return answer