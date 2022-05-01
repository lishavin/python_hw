list = []

while True:
    item = input("Enter anything: ")
    if(item == "q"):
        break  
    else:
        list.append(item)

print(list)
