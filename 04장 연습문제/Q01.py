# 함수
def is_odd(num):
    if num % 2 == 1:
        # print("홀수입니다!") -> print 할 필요없이 결과값으로 return 해주면 된다
        return True
    else:
        # print("짝수입니다!") -> print 할 필요없이 결과값으로 return 해주면 된다
        return False


print(is_odd(1))
print(is_odd(2))
