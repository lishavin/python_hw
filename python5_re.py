import random
import time

menu=[]

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")

while True:
    if(len(menu)==5):
        break
    else:
        item = input("메뉴 추가: ")
        if(item not in menu):
            menu.append(item)
        else:
            del menu[menu.index(item)]
            menu.append(item)
            print('이미 있는 메뉴에요! 다른 메뉴를 입력해주세요.')
    print('현재 메뉴 수=', len(menu))


for x in range(1,4):
    print(4-x)
    time.sleep(1)

print(menu)
print('과연 오늘의 메뉴는?')

for x in range(1,4):
    print(4-x)
    time.sleep(1)

a = random.choice(menu)
print('오늘의 메뉴는', menu.index(a)+1,'번째 메뉴,', a, '입니다.')

            
