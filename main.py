import time
import random

def welcome(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def selection_sort(data):
    n = 0
    for i in range(len(data)):
        n += 1
        m_idx = i
        print(f"list = {data}")
        for j in range(i, len(data)):
            if data[j] < data[m_idx]:
                m_idx = j
        data[m_idx], data[i] = data[i], data[m_idx]
        while True:
            ans = list(map(int, input(f"請輸入排序第{n}次後的清單(數字用空格間隔): ").split()))
            if ans == data:
                print("答對了!")
                break
            else:
                print("答錯了")

def insertion_sort(data):
    n = 0
    for i in range(1, len(data)):
        n += 1
        print(f"list = {data}")
        x = i
        while x > 0 and data[x-1] > data[x]:
            data[x], data[x-1] = data[x-1], data[x]
            x -= 1
        while True:
            ans = list(map(int, input(f"請輸入排序第{n}次後的清單(數字用空格間隔): ").split()))
            if ans == data:
                print("答對了!")
                break
            else:
                print("答錯了")

def bubble_sort(data):
    n = 0
    for i in range(len(data)-1, 0, -1):
        n += 1
        print(f"list = {data}")
        for j in range(0, i):
            if data[j+1] < data[j]:
                data[j], data[j+1] = data[j+1], data[j]
        while True:
            ans = list(map(int, input(f"請輸入排序第{n}次後的清單(數字用空格間隔): ").split()))
            if ans == data:
                print("答對了!")
                break
            else:
                print("答錯了")

            
messages = [
    "歡迎來到排序大挑戰!",
    "有4種排序法: 1.選擇排序 2.插入排序 3.氣泡排序",
    "有兩種難度: 1.清單內5個數 2.清單內7個數 "
]

for i in messages:
    welcome(i, delay=0.05)
    time.sleep(0.5)

List = []
select = int(input("請選擇一個："))
difficulty = int(input("請選擇難度："))

if difficulty == 1:
    for i in range(5):
        n = random.randint(0, 9)
        List.append(n)
elif difficulty == 2:
    for i in range(7):
        n = random.randint(0, 9)
        List.append(n)

if select == 1:
    selection_sort(List)
elif select == 2:
    insertion_sort(List)
elif select == 3:
    print("「從大排到小」")
    bubble_sort(List)


l_messenges = [
    "恭喜你完成遊戲",
    "太強了!!!"
]
if difficulty == 1:
    l_messenges.append("下次可以試試困難版!")

delay=0.5
for i in l_messenges:
    welcome(i, delay=0.05)
    time.sleep(0.5)
