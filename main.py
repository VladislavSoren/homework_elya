repeats = 1
while repeats <= 5:
    number = int(input("введите число от 1 до 10"))
    if number in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
         print("число принято")
         break
    repeats += 1      