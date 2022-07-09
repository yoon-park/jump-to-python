# 라이브러리 random
import random

numbers = []
while len(numbers) < 6:
    num = random.randint(1, 45)
    if num not in numbers:  # if 조건문을 이렇게 걸 수도 있다..
        numbers.append(num)

print(numbers)
