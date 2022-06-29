# 딕셔너리
a = dict()
a["name"] = "python"
a[("a",)] = "python"
# a[[1]] = "python" -> 리스트는 변할 수 있는 값이므로 key가 될 수 없다
a[250] = "python"
print(a)
