symbol = input ("Please enter one of the following: +, -, x, / ")
print("You chose {}.".format(symbol))
num1 = input("Please enter first number: ")
num2 = input("Please enter second number: ")
print("You chose {} {} {} ".format(num1, symbol, num2))
try:
    num1 =float(num1)
    num2=float(num2)
    if symbol == '+':
        ans=num1+num2
        print("You chose {} {} {} = {} ".format(num1, symbol, num2, ans))
    elif symbol == '-':
        ans=num1-num2
        print("You chose {} {} {} = {} ".format(num1, symbol, num2, ans))
    elif symbol == 'x':
        ans=num1*num2
        print("You chose {} {} {} = {} ".format(num1, symbol, num2, ans))
    elif symbol == '/':
        ans=num1/num2
        print("You chose {} {} {} = {} ".format(num1, symbol, num2, ans))
    else:
        print("You entered wrong stuff ")
except:
    print("Error, please try again ")



