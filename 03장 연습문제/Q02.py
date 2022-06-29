# while문
a = 0
sum = 0
while a < 1000:
    a += 1
    if a % 3 == 1:
        continue
    if a % 3 == 2:
        continue
    sum += a
print(sum)

"""
a를 처음에 1로 선언하고 while문 안쪽을

    if a % 3 = 0:
        sum += a
    a += 1

이렇게 구성하는 편이 더 간단하다
"""
