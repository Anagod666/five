import random


def is_correct(a):
    try:
        int(a)
    except ValueError:
        exit("Некорректный ввод")
    if int(a) > 3 or int(a) < 1:
        exit("Некорректный ввод")
    return int(a)


move = 0
S = random.randint(4, 30)
print("Игра в камни, число камней - ", S)
while S > 0:
    if move % 2 == 0:
        a = is_correct(input("Ваш ход, введите число от 1 до 3: "))
        S -= a
        print("Камней стало - ", S)
        move += 1
    else:
        a = random.randint(1, 3)
        print("Компьютер ходит: ", a)
        S -= a
        print("Камней стало - ", S)
        move += 1

if move % 2 == 0:
    print("Конец игры, победил Компьютер")
else:
    print("Вы выиграли!")
