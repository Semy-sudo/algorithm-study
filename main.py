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
                    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
s = solution(genres,plays)
print(s)