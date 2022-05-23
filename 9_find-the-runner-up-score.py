import re


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = list(set(arr))
    list.sort(x)
    print(x[-2])