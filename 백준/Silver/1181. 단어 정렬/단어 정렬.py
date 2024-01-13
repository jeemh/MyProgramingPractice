

testcase = int(input())

text = [None]*testcase
for i in range(testcase):
    text[i] = input()

text = list(set(text))
text.sort()
text.sort(key=len)

for i in range(len(text)):
    print(text[i])
