# string is immutable, ordered and text represenation in unicode

str1 = "I am a programmer."

# multi-line string
str2 = """I am a doctor and 
I love my job."""

print(str1)
print(str2)

str3 = "Hello, World!"
print(str3[0])  # H
print(str3[-1])  # !

# str3[2] = 'a' # TypeError: 'str' object does not support item assignment

# substring
print(str3[0:5])  # Hello
print(str3[1:5:2])  # el
print(str3[::-1])  # reverse the string

str4 = "Prabhat"
for char in str4:
    print(char)

for index, char in enumerate(str4):
    print(index, char)

# strip 
str5 = "   Hello, World!   "
print(str5.strip())  # "Hello, World!"

# upper, lower, endswith, startswith
str6 = "Python is fun!"
print(str6.upper())  # "PYTHON IS FUN!"
print(str6.lower())  # "python is fun!"
print(str6.endswith("fun!"))  # True
print(str6.startswith("Python"))  # True

cnt = str6.count("o")
print(cnt)  # 2

# find, replace
print(str6.find("Python"))  # 0 return first index
print(str6.find("Java"))  # -1 not found
print(str6.replace("Python", "Java"))  # "Java is fun!" only when the Python is found, it will replace it with Java 


# split, join
str7 = "Python is fun!"
words = str7.split()  # default separator is whitespace
print(words)  # ['Python', 'is', 'fun!']
str8 = "Python,is,fun!"
words = str8.split(",")  # separator is comma
print(words)  # ['Python', 'is', 'fun!']
str9 = " ".join(words)  # join the words with space
print(str9)  # "Python is fun!"



# %, .format() method and f-string
name = "John"
age = 30
# using % operator
print("My name is %s and I am %d years old." % (name, age))
# using .format() method
print("My name is {} and I am {} years old.".format(name, age))
# using f-string
print(f"My name is {name} and I am {age} years old.")