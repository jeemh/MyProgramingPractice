import sys
from collections import deque

dq = deque([])

testcase = int(sys.stdin.readline())

cnt = 0
for i in range(testcase):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        cnt += 1
        dq.append(int(command[1]))
    elif command[0] == 'pop':
        if dq:
            cnt -= 1
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(cnt)
    elif command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if dq:
            element = dq.popleft()
            dq.appendleft(element)
            print(element)
        else:
            print(-1)
    elif command[0] == 'back':
        if dq:
            element = dq.pop()
            dq.append(element)
            print(element)
        else:
            print(-1)
    