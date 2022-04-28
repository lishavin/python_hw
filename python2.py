a = {}

a["이름"] = "이효빈"
a["나이"] = "22살"
a["학번"] = "2020121118"
a["학과"] = "경제학부"
a["생일"] = "20010331"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]

print(a)
print(len(a))
print()

a=dict(이름 = "이효빈", 나이 = "22살", 학번 = "2020121118", 학과 = "경제학부", 생일 = "20010331")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))