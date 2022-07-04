# 함수와 여러개의 입력값
def avg(*args):
    result = 0
    for i in args:
        result = result + i
    return result / len(args)


print(avg(1, 2, 3, 4))
