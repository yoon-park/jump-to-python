# if문과 elif
a = "Life is too short, you need python"

if "wife" in a:  # 거짓이다
    print("wife")
elif "python" in a and "you" not in a:  # 거짓이다
    print("python")
elif "shirt" not in a:  # 참이다 -> 가장 먼저 참이므로 실행된다
    print("shirt")
elif "need" in a:  # 참이다
    print("need")
else:
    print("none")
