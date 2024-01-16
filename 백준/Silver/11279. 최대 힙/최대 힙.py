import sys
import heapq

testcase = int(sys.stdin.readline())
heap = []
cnt = 0
for i in range(testcase):
    x = int(sys.stdin.readline())
    if x == 0:
        if cnt == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
            cnt -= 1
    else:
        heapq.heappush(heap, -x)
        cnt += 1