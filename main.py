import pyautogui as pg
import time

def cursor(interval):
    print("start")
    while True:
        pg.moveTo(1, 1)
        time.sleep(interval)
        pg.moveTo(10, 10)

print("カーソル移動の間隔時間を入力(秒)")
interval = int(input())
cursor(interval)