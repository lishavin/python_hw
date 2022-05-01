total_list = []

while True:
    type = input("Enter a fruit type(q to quit): ")
    if(type == "q"):
        break
    else: 
        total_list.append({"question" : type, "answer" : ""})
        weight = input("Enter the weight in kg: ")

for i in total_list:
    i["answer"] = weight

print(total_list)


