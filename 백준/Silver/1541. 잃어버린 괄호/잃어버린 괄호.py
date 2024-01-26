import sys

mod = sys.stdin.readline().split('-')
sum = 0
for i in mod[0].split('+'):
    sum += int(i)
for i in mod[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)
