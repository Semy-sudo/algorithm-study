def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
      bin_str = bin(arr1[i] | arr2[i])[2:] #숫자에 대해 or연산 후 2진수로 바꾸고 슬라이싱
      answer.append(("0"*(n-len(bin_str))+ bin_str).replace("1","#").replace("0"," "))

    

    return answer

n = 5
arr1 = [9,20,28,18,11]
arr2 = [9,1,21,17,28]
print(solution(n, arr1, arr2))
#이진법으로 바꾼후 arr1+arr2

 
