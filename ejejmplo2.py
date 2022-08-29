fizzbuzz = ""
for x in range(1,101):
    if (x%3 == 0) & (x%5 != 0):
        fizzbuzz = fizzbuzz + "fizz\n"

    elif (x%3 != 0) & (x%5 == 0):
        fizzbuzz = fizzbuzz + "buzz\n"

    elif x%15 == 0:
        fizzbuzz = fizzbuzz + "fizzbuzz\n"    

    else:
        fizzbuzz = fizzbuzz + f"{x}\n"    

print(fizzbuzz)