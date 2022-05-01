mydic = {}

while True:
    type = input("Enter a fruit type (q to quit): ")
    if(type=='q'):
        break
    else:
        mydic[type]=''
        weight = input("Enter the weight in kg: ")
        mydic[type]=weight

print(mydic)