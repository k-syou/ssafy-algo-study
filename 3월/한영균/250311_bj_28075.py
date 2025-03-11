'''
스파이 민겸이는 이웃 나라와의 평화를 위해 
N 일간 임무를 수행한다.

민겸이는 정보 수집과 감시 2가지 임무를 수행한다. 각 임무는 수족관, 시청, 학교에서 수행할 수 있다. 두 임무는 성격이 크게 다르기 때문에 하루에 한 가지 임무만 수행할 수 있으며, 수족관, 시청, 학교는 멀리 떨어져 있기 때문에 하루에 한 가지 장소에서만 임무를 수행할 수 있다. 또한, 민겸이는 반드시 하루에 최소 하나의 임무를 수행해야 한다.



다시 말해, 민겸이는 하루에 위 표의 6가지 행동 중 하나를 선택하여 할 수 있다.

민겸이는 각 장소에서 각 임무를 수행할 때, 임무 완수를 위한 진척도를 얻을 수 있다. 
그러나 민겸이는 스파이이기 때문에, 같은 장소에서 오래 근무하면 사람들의 눈에 띄어 얻을 수 있는 진척도가 낮아진다. 
민겸이가 전날에 임무를 수행한 곳과 같은 장소를 선택하면 그 날은 원래의 절반에 해당하는 진척도만 얻을 수 있다. 
이때, 장소가 같다면 임무가 달라도 얻는 진척도는 원래의 절반이 됨에 유의하자.

민겸이의 기여도는 얻은 진척도의 합이다. 각 장소에서 각 임무를 수행했을 때 얻을 수 있는 진척도가 주어질 때 민겸이가 
M 이상의 기여도를 얻을 수 있는 임무 수행 방법이 몇 가지인지 구하라.
'''

n, m  = list(map(int, input().split()))  # N : 수행일수 , M : 요구 최소 기여도 
arr = [list(map(int, input().split())) for _ in range(2)]
cnt = 0

def s(d, prev, total):
    global cnt
    if d == n+1:
        if total >= m:
            cnt += 1
        return
    for work in range(2):
        for place in range(3):
            if place == prev:
                s(d+1, place, total+arr[work*3+place]//2)
            else:
                s(d+1, place, total+arr[work*3+place])

s(1, -1, 0)
print(cnt)

n, m = map(int, input().split())
progress = list(map(int, input().split()))+list(map(int, input().split()))
ans = 0
 
 
def recursion(d, prev, total):
    global ans
    if d == n+1:
        if total >= m:
            ans += 1
        return
    for work in range(2):
        for place in range(3):
            if place == prev:
                recursion(d+1, place, total+progress[work*3+place]//2)
            else:
                recursion(d+1, place, total+progress[work*3+place])
 
 
recursion(1, -1, 0)
print(ans)

def recursion(d, prev, total):
    global ans
    if d == n+1:
        if total >= m:
            ans += 1
        return
    for work in range(2):
        for place in range(3):
            if place == prev:
                recursion(d+1, place, total + progress[work][place] // 2)
            else:
                recursion(d+1, place, total + progress[work][place])

n, m = map(int, input().split())
progress = [list(map(int, input().split())) for _ in range(2)]  # 2차원 리스트로 저장
ans = 0
recursion(1, -1, 0)
print(ans)
