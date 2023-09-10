# write a basic calculator program that collect arbitrary number of inputs

def add_numbers(*args):
    result = sum(args)
    return(result)
    
def subtract_number(*args):
    result = args[0]
    for num in args[1: ]:
        result -= num
    return result


number = [x for x in input("Enter number: ")].split(" ")


choice = input("Select choice: ")

if choice == "1":
    print(add_numbers(number))
elif choice == "2":
    print(subtract_number())