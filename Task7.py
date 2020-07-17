# -*- coding: utf-8 -*-
Year = int(input())
if Year % 4 != 0:
    print("Обычный")
elif Year % 100 == 0:
    if Year % 400 == 0:
        print("Висакосный")
    else:
        print("Обычный")
else:
     print("Висакосный")               