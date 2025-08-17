import math
import sys
import os

def clrsc():
        if os.name == 'nt':
            os.system('cls')
    
        else:
            os.system('clear')

def main():
    print("---------------------------------------------------")
    print("|                                                 |")
    print("|                    MAIN MENU                    |")
    print("|                                                 |")
    print("|    1. Addition                 2. Subtraction   |")
    print("|                                                 |")
    print("|    3. Multiplication           4. Division      |")
    print("|                                                 |")
    print("|    5. Power                    6. Root          |")
    print("|                                                 |")
    print("|                    99. Quit                     |")
    print("|                                                 |")
    print("---------------------------------------------------")

    mainmenuchoice = input("Enter you choice : ")
    clrsc()

    if (int(mainmenuchoice) == 1):
        clrsc()
        addition()

    elif (int(mainmenuchoice) == 2):
        clrsc()
        subtraction()

    elif (int(mainmenuchoice) == 3):
        clrsc()
        multiplication()
    elif (int(mainmenuchoice) == 4):
        clrsc()
        division()

    elif (int(mainmenuchoice) == 5):
        clrsc()
        power()

    elif (int(mainmenuchoice) == 6):
        clrsc()
        root()

    elif (int(mainmenuchoice) == 99):
        clrsc()
        quit()
    
    else:
        print("ERROR, ENTER CORRECT OPTION !!!!!!!!!")
        input("Press Enter to continue...")
        clrsc()
        main()




def addition():
    try:
        add1 = input("Enter first number : ")
        add2 = input("Enter second number : ")
        result = float(add1)+float(add2)
    except ValueError:
        print("Invalid number entered")
    else:
        print("Your answer is : ",result)

    


    input("Press Enter to exit...")
    clrsc()
    main()

def subtraction():
    try:
        sub1 = input("Enter first number : ")
        sub2 = input("Enter second number : ")
        result = float(sub1)-float(sub2)

    except ValueError:
        print("Invalid number entered")
    
    else:
        print("Your answer is : ", result)
    
    input("Press Enter to exit...")
    clrsc()

    main()

def multiplication():
    try:
        mul1 = input("Enter first number : ")
        mul2 = input("Enter second number : ")
        result = int(mul1)*int(mul2)
    except ValueError:
        print("Invalid number entered")
    else:
        print("Your answer is : ", result)
        

    input("Press Enter to exit...")
    clrsc()

    main()


def division():
    # div1 = input("Enter first number : ")
    # div2 = input("Enter second number : ")
    # print("Your answer is : ", float(div1)/float(div2))

    try:
        div1 = input("Enter first number: ")
        div2 = input("Enter second number: ")
        result = float(div1) / float(div2)

    except ZeroDivisionError:
        print("Not defined") 

    except ValueError:
        print("Invalid number entered")

    else:
        print("Your answer is :", result)


    input("Press Enter to exit...")
    clrsc()

    main()

def power():
    try:
        pow1 = input("Enter number : ")
        pow2 = input("Enter number of power : ")
        result = float(pow1)**float(pow2)
    except ValueError:
        print("Invalid number entererd")
        
    except OverflowError:  
        print("Result is too large to handle")
        input("Press Enter to exit...")
        main()
        return

    else:
        print("Your answer is : ", result)

    input("Press Enter to exit...")
    clrsc()

    main()

def root():
    try:
        roo = float(input("Enter the number : "))
        square__root = math.sqrt(roo)
        
    except ValueError:
        print("Invalid number entered")
    else:
        print("The square root of ",roo," is ", square__root)

    input("Press Enter to exit...")
    clrsc()

    main()

def quit():
    print("Quitting The Program...")
    sys.exit(0)


main()
