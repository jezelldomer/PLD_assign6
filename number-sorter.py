#Create a program that ask 4 numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))
num4 = float(input("Enter your fourth number: "))

def high_low(num1, num2, num3, num4):
 if num1 >= num2 and num1 >= num3 and num1 >= num4:
        if num2 >= num3 and num2 >= num4:
            if num3 >= num4:
                _numbers = [num1, num2, num3, num4]
                print(f"The numbers are in the following order:{_numbers} ")
            elif num4 >= num3:
                _numbers = [num1, num2, num4, num3]
                print(f"The numbers are in the following order:{_numbers} ")
        elif num3 >= num2 and num3 >= num4:
            if num2 >= num4:
                _numbers = [num1, num3, num2, num4]
                print(f"The numbers are in the following order:{_numbers} ")
        elif num4 >= num2:
                _numbers = [num1, num3, num4, num2]
                print(f"The numbers are in the following order:{_numbers} ")
        elif num4 >= num2 and num4 >= num3:
            if num3 >= num2:
                _numbers = [num1, num4, num3, num2]
                print(f"The numbers are in the following order:{_numbers} ")
            elif num2 >= num3:
                _numbers = [num1, num4, num2, num3]
                print(f"The numbers are in the following order:{_numbers} ")
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        if num1 >= num3 and num1 >= num4:
            if num3 >= num4:
                _numbers = [num2, num1, num3, num4]
                print(f"The numbers are in the following order:{_numbers} ")
elif num4 >= num3:
                _numbers = [num2, num1, num4, num3]
                print(f"The numbers are in the following order:{_numbers} ")
        elif num3 >= num1 and num3 >= num4:
            if num1 >= num4:
                _numbers = [num2, num3, num1, num4]
                print(f"The numbers are in the following order:{_numbers} ")
            elif num4 >= num1:
                _numbers = [num2, num3, num4, num1]
                print(f"The numbers are in the following order:{_numbers} ")
        elif num4 >= num1 and num4 >= num3:
            if num1 >= num3:
                _numbers = [num2, num4, num1, num3]
                print(f"The numbers are in the following order:{_numbers} ")
            elif num3 >= num1:
                _numbers = [num2, num4, num3, quan1]
                print(f"The numbers are in the following order:{_numbers} ")
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        if num1 >= num2 and num1 >= num4:
            if num2 >= num4:
                _numbers = [num3, num1, num2, num4]
                print(f"The numbers are in the following order:{_numbers} ")
            elif num4 >= num2:
                _numbers = [num3, num1, num4, num2]
                print(f"The numbers are in the following order:{_numbers} ")
