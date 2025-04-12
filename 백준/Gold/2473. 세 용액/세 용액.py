import sys
input = sys.stdin.readline
result = [float('inf'), 0, 0, 0]

def yung(arr, n):  # arr는 정렬된 배열, n은 배열의 길이
    global result
    for s in range(n-2):  # 첫 번째 용액을 고정하고 나머지 두 용액을 탐색
        m, e = s+1, n-1  # 투 포인터 초기화
        while m < e:
            sum = arr[s] + arr[m] + arr[e]
            if abs(sum) < abs(result[0]):
                result = [sum, arr[s], arr[m], arr[e]]
            if sum > 0:
                e -= 1  # 합이 0보다 크면 큰 값을 줄여 합을 줄임
            elif sum < 0:
                m += 1  # 합이 0보다 작으면 작은 값을 늘려 합을 늘림
            else:
                return  # 합이 0인 경우 최적의 결과

n = int(input())
A = list(map(int, input().split()))
b = sorted(A)

yung(b, n)  # 함수 호출
print(result[1], result[2], result[3])  # 결과 출력
