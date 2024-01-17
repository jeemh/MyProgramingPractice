import sys

def sumOfCutTree(tree,standard):
    sum = 0
    for oneOfTree in tree:
        if oneOfTree > standard:
            sum += oneOfTree - standard
        else:
            break
    return sum

def binarySearch(tree, key, start, mid, end):
    if sumOfCutTree(tree,mid) == key or start > end:
        print(mid)
        exit()
    
    elif sumOfCutTree(tree,mid) > key:
        start = mid + 1
        mid = (start + end)//2
        
    elif sumOfCutTree(tree,mid) < key:
        end = mid - 1
        mid = (start + end)//2
        
    binarySearch(tree, key, start, mid, end)

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

maxTree = max(tree)
tree.sort(reverse=True)
# print(tree)
binarySearch(tree, m, 0, maxTree//2, maxTree)