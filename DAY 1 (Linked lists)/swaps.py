# swapping 2 numbers without using arithmetic operators or 3rd variable
a = int(input("A : "))
b = int(input("B : "))

a = a^b
b = a^b
a = a^b


print(f"After Swapping \nA : {a} \nB : {b}")
