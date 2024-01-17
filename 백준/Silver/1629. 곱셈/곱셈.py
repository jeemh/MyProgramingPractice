# def mulAndRest(a,b,c):
#     # if b == 1:
#     #     return 1
#     # return mulAndRest(a,b-1,c)*a%c
#     if b == 1:
#         return a%c
#     return a*mulAndRest(a,b//2,c)%c*a*mulAndRest(a,b-(b//2),c)%c
#     # if b%2==0:
#     #     y = mulAndRest(a,b//2,c)*a%c
#     # else:
#     #     y = mulAndRest(a,b//2+1,c)*a%c
#     # return a*x%c*a%c*y%c

# a, b, c = map(int, input().split())
# print(mulAndRest(a,b,c))
# # sum = 1
# # for i in range(b):
# #     sum %= c
# #     sum *= a
# # print(sum%c)
def mulAndRest(a, b, c):
    if b == 0:
        return 1

    half_result = mulAndRest(a, b // 2, c)
    result = half_result * half_result % c

    if b % 2 == 1:
        result = result * a % c
    return result

a, b, c = map(int, input().split())
print(mulAndRest(a, b, c))

