truc = []
machin = [0.07, 0.42, 0.36, 0.59, 0.01]
print(f"truc: {truc}, machin:{machin}")

for i in range(0, 4):
    print(i)

for i in range(4, 8):
    print(i)

for i in range(2, 9, 2):
    print(i)


def appartient(item, list):
    if item in list:
        print(f"{item} in chose")
    else:
        print(f"not {item} in chose")


chose = [0, 1, 2, 3, 4, 5]
appartient(3, chose)
appartient(6, chose)
