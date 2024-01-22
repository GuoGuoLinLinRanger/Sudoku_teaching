print("Calculator v.1")
def addition(x,y):
    print(x+y)
def substraction(x,y):
    print(x-y)
def multiplication(x,y):
    print(x*y)
def division(x,y):
    print(x/y)

while True:
    choice = input( "Choose the number of the operation : 1.addition  2.substraction  3.multiplication  4.division : ")
    if choice in("1","2","3","4"):
        if choice == "1" :
            x = float(input("what is your first number: "))
            y = float(input("what is your second number: "))
            print(addition(x,y))
        if choice == "2":
            x = float(input("what is your first number: "))
            y = float(input("what is your second number: "))
            print(substraction(x,y))
        if choice == "3":
            x = float(input("what is your first number: "))
            y = float(input("what is your second number: "))
            print(multiplication(x,y))
        if choice == "4":
            x = float(input("what is your first number: "))
            y = float(input("what is your second number: "))
            print(division(x,y))
    else:
        print("Invalid answer")

    