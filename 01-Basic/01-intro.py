print("Hello, World!")

name : str = input("What is your full name? \n")
print(f"Hello, {name}")

age : int = int(input("What is your age \n"))
print(f"{name} age is {age}")


first_name , last_name  = name.split(" ")
print(f"First Name : {first_name} \nLast Name : {last_name}")


# alternative way when you know the length
first_name = name[:8]
print(f"First Name : {first_name}")


