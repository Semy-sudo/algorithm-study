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
    print(roads)
    




    return len(roads)

dirs = "ULURRDLLU"
s = solution(dirs)
print(s)

