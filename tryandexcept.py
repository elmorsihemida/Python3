"""
try => let you test a block of code for errors
except => let you handle errors
else => let you execute code when there is no error
finally => block lets you execute code, regardless of the result of the try and except blocks

"""
try:
    num = int(input("Enter your num here: "))
    name = input("Enter your name here: ")
    result = 10 / num
except ZeroDivisionError as err:
    print(f"Error: {err}")
except ValueError as value:
    print(f"Error: {value}")
else:
    print(f"Hello {name}, your input is success")
finally:
    try:
        print(f"Your result is: {result}")
    except NameError:
        print("Wrong num")
