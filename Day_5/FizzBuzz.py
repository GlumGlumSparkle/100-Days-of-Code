for number in range(1,101):
    if number % 3 == 0:
        if number % 5 == 0:
            print(number, "FizzBuzz")
        else:
            print(number, "Fizz")
    elif number%5 == 0:
        print(number, "Buzz")
    else:
        print(number)


