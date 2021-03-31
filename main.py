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








m = "CC#BCC#BCC#BCC#B"#16
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
s = solution(m,musicinfos)
print(s)

