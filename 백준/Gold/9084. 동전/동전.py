testCase = int(input())

for _ in range(testCase):
    numOfCoin = int(input())
    coins = list(map(int, input().split(' ')))
    targetAmount = int(input())

    memo = [[0] * (targetAmount+1) for _ in range(len(coins)+1)]
    for coin in memo:
        coin[0] = 1
    
    for col in range(len(memo)-1):
        for row in range(1,len(memo[col])):
            if row >= coins[col]:
                memo[col][row] += memo[col][row-coins[col]]
        memo[col+1] = memo[col]
    print(memo[len(coins)][targetAmount])

    # 참고 블로그 : https://d-cron.tistory.com/23