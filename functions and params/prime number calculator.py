def prime_checker(number):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number.")    
    else:
        print("It's not a prime number.")
#Write your code above this line 👆
#Don't change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
