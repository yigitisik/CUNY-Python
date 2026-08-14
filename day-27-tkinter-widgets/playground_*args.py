def add(*args):
    total = 0
    for n in args:
        total += n
    return total

continue_adding = True
while continue_adding:
    num = input("Put in numbers to add (space-separated), or type 'exit' to quit: ")
    if num.lower() == "exit":
        continue_adding = False
    else:
        try:
            numbers = [int(n) for n in num.split()]
            sum = add(*numbers)
            print(f"Sum of numbers given: {sum}")
        except ValueError:
            print("Please enter valid integers separated by spaces.")

