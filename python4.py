total_list = []

while True:
    type = input("Enter a fruit type(q to quit): ")
    if type == "q":
        break
    else: 
        total_list.append({"question" : type, "answer" : ""})
for i in total_list:
    print(i["question"])
    weight = input("Enter the weight in kg: ")
    i["answer"] = weight

print(total_list)


