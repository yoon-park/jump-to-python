# 라이브러리 os
import os
import subprocess

"""
result = os.popen("dir")
print(result.read())

원래라면 이 풀이면 끝나지만, 한국어가 포함되어 있어
UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 147: illegal multibyte sequence
이런 에러가 발생한다.

따라서 os.popen 대신 subprocess.Popen을 사용하는 방식으로 아래와 같이 풀면 된다고 한다.
"""

p = subprocess.Popen("cmd /u /c dir", stdout=subprocess.PIPE)
result = p.communicate()
text = result[0].decode("u16")
print(text)
