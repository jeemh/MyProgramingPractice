testcase = int(input())

num = [None]*testcase
for i in range(testcase):
    num[i] = int(input())
num = sorted(num)
for i in range(testcase):
    print(num[i])