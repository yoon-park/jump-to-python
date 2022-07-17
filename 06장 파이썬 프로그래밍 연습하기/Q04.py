# 간단한 메모장 만들기
import sys

option = sys.argv[1]

if option == "-a":
    text = sys.argv[2]
    f = open("memo.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()

if option == "-r":
    f = open("memo.txt", "r")
    memo = f.read()
    print(memo)
    f.close()
