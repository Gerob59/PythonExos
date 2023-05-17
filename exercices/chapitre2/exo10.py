import math

for x in range(-3, 4):
    try:
        print(math.sin(x) / x)
    except ZeroDivisionError:
        print("on ne peux pas diviser par 0")
