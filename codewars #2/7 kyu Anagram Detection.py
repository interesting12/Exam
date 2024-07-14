def smaller(arr):
    list1 = []
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    num3 = int(input("enter num3: "))
    list1.append(num1)
    list1.append(num2)
    list1.append(num3)
    print(f"original = {list1}")
    print(f"smaller = {list1 [::-1]}")
smaller(1)


   