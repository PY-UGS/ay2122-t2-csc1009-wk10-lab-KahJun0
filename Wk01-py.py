name = input("Please enter your name: ")
print(f"Hello, I am {name}")

module_code = input("Please enter the module code: ")

if module_code == "CSC1006":
    print("Mathematics 2")
elif module_code == "CSC1007":
    print("Operating Systems")
elif module_code == "CSC1008":
    print("Data Structures and Algorithms")
elif module_code == "CSC1009":
    print("Object Oriented Programming")
elif module_code == "CSC1010":
    print("Computer Networks")
else:
    print("Module not found")

for i in reversed(range(66, 103)):
    print(i)

