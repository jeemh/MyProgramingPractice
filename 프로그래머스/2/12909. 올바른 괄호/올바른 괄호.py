def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            if stack[-1] != '(':
                return False
            else:
                stack.pop()
                
    if len(stack) != 0:
        return False
    
    return True