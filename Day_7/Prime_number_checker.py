
# Function to determine prime and compound numbers
def prime_checker(number):
    if number>1:
        for x in range(2, number):
            if number%x == 0:
                print(f"Number {number} is compound number")
                break
        else:
            print(f"Number {number} is prime number")
    else:
        print(f"Number {number} is not a prime number as it is smaller than 1")

# Input and function return
n = int(input("Check this number: "))
prime_checker(number=n)

