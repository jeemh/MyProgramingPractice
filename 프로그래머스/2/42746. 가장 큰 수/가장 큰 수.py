def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x:x*3, reverse = True)
    for num in numbers:
        answer += num
    
    return str(int(answer))