from re import A
import time
import random

menu = []
result = []

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")

  
while True:    
    item = input("메뉴 추가: ")
    if(len(result) == 4):
        break
    else: 
        for i in menu:
            if i not in result:
                result.append(i)
            else:
                del menu[item]
                menu.append(item)
                print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
        print("현재 메뉴 수: ", len(result))

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(result)
print("과연 오늘의 메뉴는?")
time.sleep(1)

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

choice = random.choice(result)
print("오늘의 메뉴는 ", result.index(choice)+1, "번째 메뉴,", choice, "입니다.")
