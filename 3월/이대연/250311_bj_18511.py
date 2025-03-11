# 18511_큰_수_구성하기
import sys
sys.stdin = open("input.txt","r")




N, K = map(int,input().split())    # N, K 입력받기
elements = list(map(int,input().split()))   # K의 원소들 입력받기

elements.sort(reverse=True) # 원소들 오름차순
numbers = [] # 숫자 N을 문자열로 바꿔서 한 글자씩 numbers 리스트에 추가
for i in range(len(str(N))):
    numbers.append(int(str(N)[i]))
print(elements)
print(numbers)

min_v =

