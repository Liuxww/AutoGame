import time
from pymouse import PyMouse

mouse = PyMouse()


def check(y, d, h, m):
    while True:
         if time.localtime().tm_mon == y and time.localtime().tm_mday == d and time.localtime().tm_hour == h and time.localtime().tm_min == m:
             mouse.click(525, 525, button=1, n=3)
             print('结束')
             break


def main():
    print("哪月：")
    year = int(input())
    print("哪日：")
    day = int(input())
    print("哪时：")
    hour = int(input())
    print("哪分：")
    m = int(input())
    print("开始")
    check(year, day, hour, m)


if __name__ == '__main__':
    main()