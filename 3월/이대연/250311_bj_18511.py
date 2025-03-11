# 18511_큰_수_구성하기
import sys
sys.stdin = open("input.txt","r")

N, K = int(input().split())     # N, K 입력받기
elements = list(input().split())    # K의 원소들 입력받기

max_num = 0    # 최대값을 구하기 위한 변수
temp = []      # 숫자를 string으로 받아서 리스트에 넣은 뒤 합치기 위해 빈 리스트 생성

