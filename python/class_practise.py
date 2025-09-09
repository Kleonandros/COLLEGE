class calc:
    def add(self):
        print(f"Sum of {a} and {b} is : ", a+b)
    def sub(self):
        print(f"Difference of {a} and {b} is : ", a-b)
    def mul(self):
        print(f"Product of {a} and {b} is : ", a*b)
    def div(self):
        print(f"Division of {a} and {b} is : ", a/b)
ob = calc()

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter choice\n1. add\n2.sub\n3.mul\n4.div\n"))

if c == 1:
    ob.add()
elif c == 2:
    ob.sub()
elif c == 3:
    ob.mul()
elif c == 4:
    ob.div()

else:
    print("Error")
