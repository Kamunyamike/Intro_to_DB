number = 1
while number <= 100:
    number += 1
    if number%5 == 0 or number%3 == 0:
        print(number)
        number += 1