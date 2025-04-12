import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def build_segment_tree(tree, arr, node, start, end):
    if start == end:
        tree[node] = (arr[start], start + 1)  # (값, 인덱스)
    else:
        mid = (start + end) // 2
        build_segment_tree(tree, arr, 2 * node + 1, start, mid)
        build_segment_tree(tree, arr, 2 * node + 2, mid + 1, end)
        tree[node] = min(tree[2 * node + 1], tree[2 * node + 2])
        
def update_segment_tree(tree, idx, value, node, start, end):
    if start == end:
        tree[node] = (value, start + 1)
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update_segment_tree(tree, idx, value, 2 * node + 1, start, mid)
        else:
            update_segment_tree(tree, idx, value, 2 * node + 2, mid + 1, end)
        tree[node] = min(tree[2 * node + 1], tree[2 * node + 2])

def query_segment_tree(tree, l, r, node, start, end):
    if r < start or end < l:
        return (float('inf'), float('inf'))
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    left_query = query_segment_tree(tree, l, r, 2 * node + 1, start, mid)
    right_query = query_segment_tree(tree, l, r, 2 * node + 2, mid + 1, end)
    return min(left_query, right_query)

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]

# 세그먼트 트리 초기화 및 구축
segment_tree = [0] * (4 * n)
build_segment_tree(segment_tree, arr, 0, 0, n - 1)

# 쿼리 처리
results = []
for query in queries:
    if query[0] == 1:  # 업데이트
        i, v = query[1] - 1, query[2]
        update_segment_tree(segment_tree, i, v, 0, 0, n - 1)
    elif query[0] == 2:  # 최소값 인덱스 찾기
        i, j = query[1] - 1, query[2] - 1
        result = query_segment_tree(segment_tree, i, j, 0, 0, n - 1)
        results.append(result[1])

# 결과 출력
for result in results:
    print(result)
