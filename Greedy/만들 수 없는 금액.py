#입력
n = int(input())
data = list(map(int, input().split()))
#화폐단위를 기준으로 오름차순 정렬
data.sort()

#특정금액(target)을 만들 수 있는지 확인 (1부터 증가시키면서)
target=1
for x in data: #화폐단위가 작은 순서대로 동전을 확인
    #현재 확인하는 동전으로 target금액을 만들 수 있는지 확인
    if target<x:
        break
    #
    target+=x
print(target)
