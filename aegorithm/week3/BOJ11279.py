"""
문제 상황: x가 자연수라면 배열에 x를 추가
         x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거
         sort하고 제일 큰 값 제거? nlogn -> 시간 초과
         힙 자료구조 사용하여 logn으로 줄이기 -> 여전히 시간 초과
         뭐가 문제지
         입출력이 문제였음
한계 상황:
예외 상황: 만약 배열이 비어있는 경우 0 출력
"""
import sys
import heapq

input = sys.stdin.readline # 빠른 입출력 적용
n = int(input()) 

heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap)) # 음수로 저장된 걸 양수로 변환하며 프린트
        else:
            print(0)
    else:
        heapq.heappush(heap, -x) # 파이썬의 heapq는 최소 힙으로, 최대힙으로 구현하기 위해서는 음수로 넣기
