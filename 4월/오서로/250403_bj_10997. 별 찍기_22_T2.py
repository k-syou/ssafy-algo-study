
def recur(i):

    if i == 1:
        D[i].append('*')
        return
    
    if i == 2:
        D[i] += ['*****', '*    ', '* ***', '* * *', '* * *', '*   *', '*****']
        return

    D[i].append('*'*4*(i-1)+'*')
    D[i].append('*'+' '*4*(i-1))
    D[i].append('*'+' '+D[i-1][0]+'**')

    for arr in D[i-1][1:]:
        D[i].append('*'+' '+arr+' '+'*')
        
    D[i].append('*'+' '*(4*(i-1)-1)+'*')
    D[i].append('*'*4*(i-1)+'*')



N = int(input())

D = [[] for _ in range(N+1)] # idx를 N으로 보고 f(N)을 저장할 리스트

for i in range(1, N+1): # 1부터 시작해서 저장하기
    recur(i)
    
print(D[N][0]) # 첫 번째 줄 출력

if N > 1:
    print('*') # 두 번째 줄
    print(*D[N][2:], sep='\n') # 3 ~ 출력
